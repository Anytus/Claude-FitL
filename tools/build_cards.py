#!/usr/bin/env python3
"""Build cards.json from the fitl source tree (sellmerfud/fitl).

Usage: build_cards.py <path-to-fitl-source-root> [out.json]

Reads src/main/scala/fitl/cards/Card_NNN.scala and extracts, per card:
  number, title, type (dual/single/pivotal/coup), factionOrder,
  unshaded, shaded (or text for single/pivotal/coup), pivotalCondition,
  momentum flag, tips, botPriorities per faction.

This is a build-time tool. It is run once, by the build session, against a
source clone kept OUTSIDE the play directory. The playing session never runs
it and never has the source in reach.
"""
import json
import os
import re
import sys

CARD_RE = re.compile(
    r'object\s+Card_(\d+)\s+extends\s+EventCard\(\s*(\d+)\s*,\s*"((?:[^"\\]|\\.)*)"\s*,'
    r'\s*(DualEvent|SingleEvent)\s*,\s*(List(?:\.empty|\([^)]*\)))\s*,\s*(ListMap(?:\.empty|\((?:.|\n)*?\)\s*\)))',
    re.S,
)
PRIO_RE = re.compile(r'(US|ARVN|NVA|VC)\s*->\s*\(\s*(Critical|Performed|Ignored)\s*->\s*(Unshaded|Shaded)\s*\)')


def parse_header(lines):
    """Split the `// ...` comment header into named sections."""
    sections = {}
    current = None
    buf = []

    def flush():
        if current is not None:
            text = "\n".join(buf).strip("\n")
            sections[current] = text
        buf.clear()

    for raw in lines:
        line = raw.rstrip()
        # strip leading comment marker; tolerate the odd '///' typo
        line = re.sub(r'^\s*/{2,}\s?', '', line)
        stripped = line.strip()
        m = re.match(r'^(Unshaded Text|Shaded Text|Single Event Text|Tips|Leader Effect|(US|ARVN|NVA|VC) Pivotal event)\b\s*(.*)$', stripped)
        if m:
            flush()
            current = m.group(1)
            if current in sections:          # repeated heading (Card_048 typo)
                current += "#2"
            if m.group(3):
                buf.append(m.group(3))
            continue
        if current is None:
            if stripped == "":
                continue
            current = "Text"
        buf.append(line)
    flush()
    return sections


def clean(text):
    lines = [l.strip() for l in text.strip().splitlines()]
    return " ".join(l for l in lines if l).replace("  ", " ")


def build(src_root):
    cards_dir = os.path.join(src_root, "src", "main", "scala", "fitl", "cards")
    out = {}
    problems = []
    for fname in sorted(os.listdir(cards_dir)):
        if not re.match(r'Card_\d+\.scala$', fname):
            continue
        with open(os.path.join(cards_dir, fname), encoding="utf-8") as f:
            src = f.read()
        m = CARD_RE.search(src)
        if not m:
            problems.append(f"{fname}: could not parse EventCard header")
            continue
        num = int(m.group(2))
        title = m.group(3).replace('\\"', '"')
        etype = m.group(4)
        order = re.findall(r'\b(US|ARVN|NVA|VC)\b', m.group(5))
        prios = {fac: {"priority": p, "side": side} for fac, p, side in PRIO_RE.findall(m.group(6))}

        # Header = comment lines between the last import and the object line
        # Header = comment lines after the license block, before the object.
        # (Usually after the imports, but Card_044 puts it before `package`.)
        pre = src[: m.start()]
        pre = pre.split("OTHER DEALINGS IN THE SOFTWARE.", 1)[-1]
        header_lines = [l for l in pre.splitlines() if l.strip().startswith("//") or l.strip() == ""]
        sections = parse_header(header_lines)

        card = {
            "number": num,
            "title": title,
            "factionOrder": order,
            "botPriorities": prios,
        }
        is_coup = len(order) == 0
        pivotal_key = next((k for k in sections if k.endswith("Pivotal event")), None)
        if is_coup:
            card["type"] = "coup"
            card["leaderEffect"] = clean(sections.get("Leader Effect", ""))
        elif pivotal_key:
            card["type"] = "pivotal"
            card["pivotalFaction"] = pivotal_key.split()[0]
            body = sections[pivotal_key]
            paras = [clean(p) for p in re.split(r'\n\s*\n', body) if p.strip()]
            cond = next((p for p in paras if p.startswith("Play if")), "")
            card["pivotalCondition"] = cond
            card["text"] = " ".join(p for p in paras if p != cond)
        elif etype == "DualEvent":
            card["type"] = "dual"
            if "Unshaded Text" not in sections and "Shaded Text#2" in sections:
                # Card_048 labels both halves "Shaded Text"; first is unshaded.
                sections["Unshaded Text"] = sections["Shaded Text"]
                sections["Shaded Text"] = sections["Shaded Text#2"]
            if "Shaded Text" not in sections and "Unshaded Text#2" in sections:
                # Card_052 labels both halves "Unshaded Text"; second is shaded.
                sections["Shaded Text"] = sections["Unshaded Text#2"]
            if "Shaded Text" not in sections and "Unshaded Text" in sections:
                # Card_062 omits the "Shaded Text" heading; halves are blank-line separated.
                paras = [p for p in re.split(r'\n\s*\n', sections["Unshaded Text"]) if p.strip()]
                if len(paras) == 2:
                    sections["Unshaded Text"], sections["Shaded Text"] = paras
            card["unshaded"] = clean(sections.get("Unshaded Text", ""))
            card["shaded"] = clean(sections.get("Shaded Text", ""))
        else:
            card["type"] = "single"
            card["text"] = clean(sections.get("Single Event Text", sections.get("Text", "")))

        # MOMENTUM marker appears as its own line inside the text
        for key in ("unshaded", "shaded", "text"):
            if key in card and "MOMENTUM" in card[key]:
                card[key] = card[key].replace("MOMENTUM", "").strip()
                card.setdefault("momentum", []).append(key)
        card["tips"] = clean(sections.get("Tips", ""))

        # sanity
        if card["type"] == "dual" and (not card["unshaded"] or not card["shaded"]):
            problems.append(f"{fname}: dual card missing text")
        if card["type"] in ("single", "pivotal") and not card["text"]:
            problems.append(f"{fname}: single/pivotal card missing text")
        if card["type"] != "coup" and len(prios) != 4:
            problems.append(f"{fname}: expected 4 bot priorities, got {len(prios)}")
        out[str(num)] = card
    return out, problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    src_root = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else "cards.json"
    cards, problems = build(src_root)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=1, ensure_ascii=False, sort_keys=False)
    types = {}
    for c in cards.values():
        types[c["type"]] = types.get(c["type"], 0) + 1
    print(f"wrote {len(cards)} cards to {out_path}: {types}")
    for p in problems:
        print("PROBLEM:", p)


if __name__ == "__main__":
    main()
