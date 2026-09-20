"""Shared helpers for render.py and diff.py: load saves, derive counts, score.

Everything here is derived from the save JSON written by the fitl program
plus a few constants (piece manifest, map regions) that are printed on the
physical game components. Nothing here reads the program's source or the
Tru'ng deck order stored in the save.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAMES_DIR = os.path.join(ROOT, "games")
CARDS_PATH = os.path.join(ROOT, "cards.json")

FACTIONS = ["US", "ARVN", "NVA", "VC"]

# Force pool (all factions' total pieces). Underground/Active and Base/Tunnel
# collapse to one generic type for availability purposes.
MANIFEST = {
    "US": {"Troops": 40, "Irregulars": 6, "Bases": 6},
    "ARVN": {"Troops": 30, "Police": 30, "Rangers": 6, "Bases": 3},
    "NVA": {"Troops": 40, "Guerrillas": 20, "Bases": 9},
    "VC": {"Guerrillas": 30, "Bases": 9},
}

# Save-file piece name -> (faction, generic type, status)
PIECE_INFO = {
    "US Troop": ("US", "Troops", None),
    "US Underground Irregular": ("US", "Irregulars", "U"),
    "US Active Irregular": ("US", "Irregulars", "A"),
    "US Base": ("US", "Bases", None),
    "ARVN Troop": ("ARVN", "Troops", None),
    "ARVN Police": ("ARVN", "Police", None),
    "ARVN Underground Ranger": ("ARVN", "Rangers", "U"),
    "ARVN Active Ranger": ("ARVN", "Rangers", "A"),
    "ARVN Base": ("ARVN", "Bases", None),
    "NVA Troop": ("NVA", "Troops", None),
    "NVA Underground Guerrilla": ("NVA", "Guerrillas", "U"),
    "NVA Active Guerrilla": ("NVA", "Guerrillas", "A"),
    "NVA Base": ("NVA", "Bases", None),
    "NVA Tunneled Base": ("NVA", "Bases", "T"),
    "VC Underground Guerrilla": ("VC", "Guerrillas", "U"),
    "VC Active Guerrilla": ("VC", "Guerrillas", "A"),
    "VC Base": ("VC", "Bases", None),
    "VC Tunneled Base": ("VC", "Bases", "T"),
}

TYPE_ORDER = ["Troops", "Police", "Irregulars", "Rangers", "Guerrillas", "Bases"]

# Board regions, in display order. Space names as the program spells them.
REGIONS = [
    ("I Corps", [
        "Hue", "Da Nang", "Quang Tri-Thua Thien", "Quang Nam", "Quang Tin-Quang Ngai",
        "LOC Hue -- Khe Sanh", "LOC Hue -- Da Nang", "LOC Da Nang -- Dak To", "LOC Da Nang -- Qui Nhon",
    ]),
    ("II Corps", [
        "Kontum", "Qui Nhon", "Cam Ranh", "Binh Dinh", "Pleiku-Darlac", "Phu Bon-Phu Yen", "Khanh Hoa",
        "LOC Kontum -- Dak To", "LOC Kontum -- Qui Nhon", "LOC Kontum -- Ban Me Thuot",
        "LOC Qui Nhon -- Cam Ranh", "LOC Cam Ranh -- Da Lat", "LOC Ban Me Thuot -- Da Lat",
    ]),
    ("III Corps", [
        "An Loc", "Saigon", "Phuoc Long", "Quang Duc-Long Khanh", "Binh Tuy-Binh Thuan", "Tay Ninh",
        "LOC Saigon -- Cam Ranh", "LOC Saigon -- Da Lat", "LOC Saigon -- An Loc -- Ban Me Thuot",
    ]),
    ("IV Corps", [
        "Can Tho", "Kien Phong", "Kien Hoa-Vinh Binh", "Ba Xuyen", "Kien Giang-An Xuyen",
        "LOC Saigon -- Can Tho", "LOC Can Tho -- Chau Doc", "LOC Can Tho -- Bac Lieu", "LOC Can Tho -- Long Phu",
    ]),
    ("Laos / Cambodia", [
        "Central Laos", "Southern Laos", "Northeast Cambodia", "The Fishhook", "The Parrot's Beak", "Sihanoukville",
    ]),
    ("North Vietnam", ["North Vietnam"]),
]

THRESHOLDS = {"US": 50, "ARVN": 50, "NVA": 18, "VC": 35}
# Victory tie order (first wins ties)
TIE_ORDER = ["VC", "ARVN", "NVA", "US"]


# ---------------------------------------------------------------- loading

def list_games():
    if not os.path.isdir(GAMES_DIR):
        return []
    return sorted(d for d in os.listdir(GAMES_DIR)
                  if os.path.isdir(os.path.join(GAMES_DIR, d)) and save_numbers(d))


def save_numbers(game):
    nums = []
    for p in glob.glob(os.path.join(GAMES_DIR, game, "save-*")):
        m = re.search(r"save-(\d+)$", p)
        if m:
            nums.append(int(m.group(1)))
    return sorted(nums)


def save_path(game, n):
    return os.path.join(GAMES_DIR, game, f"save-{n:03d}")


def log_path(game, n):
    return os.path.join(GAMES_DIR, game, f"log-{n:03d}")


def default_game():
    games = list_games()
    if len(games) == 1:
        return games[0]
    env = os.environ.get("FITL_GAME")
    if env and env in games:
        return env
    if not games:
        raise SystemExit("no saved games under games/")
    raise SystemExit(f"several games under games/ ({', '.join(games)}); pass the game name or set FITL_GAME")


def load_save(path):
    with open(path, encoding="utf-8") as f:
        top = json.load(f)
    return top["game-state"]


def load_log(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        try:
            top = json.load(f)
        except json.JSONDecodeError:
            f.seek(0)
            return [l.rstrip("\n") for l in f]
    return [e["text"] for e in top["log"]]


def load_cards():
    with open(CARDS_PATH, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- pieces

def count_pieces(names):
    """names: flat list of piece names -> {faction: {generic: n}} plus statuses."""
    out = {f: {} for f in FACTIONS}
    status = {f: {} for f in FACTIONS}  # (generic, status) -> n
    for n in names:
        fac, gen, st = PIECE_INFO[n]
        out[fac][gen] = out[fac].get(gen, 0) + 1
        key = (gen, st)
        status[fac][key] = status[fac].get(key, 0) + 1
    return out, status


def faction_total(names, faction):
    return sum(1 for n in names if PIECE_INFO[n][0] == faction)


def piece_summary(names):
    """Human-readable, e.g. 'US: 2 Troops, 1 Base | NVA: 3 Guerrillas (2U 1A), 1 Base'."""
    counts, status = count_pieces(names)
    parts = []
    for fac in FACTIONS:
        if not counts[fac]:
            continue
        bits = []
        for gen in TYPE_ORDER:
            n = counts[fac].get(gen)
            if not n:
                continue
            label = gen if n != 1 else gen.rstrip("s") if gen != "Police" else gen
            if gen in ("Guerrillas", "Irregulars", "Rangers"):
                u = status[fac].get((gen, "U"), 0)
                a = status[fac].get((gen, "A"), 0)
                bits.append(f"{n} {label} ({u}U {a}A)")
            elif gen == "Bases":
                t = status[fac].get((gen, "T"), 0)
                bits.append(f"{n} {label}" + (f" ({t} Tunneled)" if t else ""))
            else:
                bits.append(f"{n} {label}")
        parts.append(f"{fac}: " + ", ".join(bits))
    return " | ".join(parts) if parts else "empty"


def available(state):
    """Manifest minus on-map minus casualties minus out-of-play, per faction/type."""
    used = {f: {} for f in FACTIONS}

    def add(names):
        for n in names:
            fac, gen, _ = PIECE_INFO[n]
            used[fac][gen] = used[fac].get(gen, 0) + 1

    for sp in state["spaces"]:
        add(sp["pieces"])
    add(state["casualties"])
    add(state["outOfPlay"])
    avail = {}
    for fac in FACTIONS:
        avail[fac] = {gen: MANIFEST[fac][gen] - used[fac].get(gen, 0) for gen in MANIFEST[fac]}
    return avail


# ---------------------------------------------------------------- spaces

def is_loc(sp):
    return sp["spaceType"] == "LOC"


def control(sp):
    if is_loc(sp):
        return "Uncontrolled"
    names = sp["pieces"]
    coin = sum(1 for n in names if PIECE_INFO[n][0] in ("US", "ARVN"))
    nva = sum(1 for n in names if PIECE_INFO[n][0] == "NVA")
    vc = sum(1 for n in names if PIECE_INFO[n][0] == "VC")
    if coin > nva + vc:
        return "COIN Control"
    if nva > coin + vc:
        return "NVA Control"
    return "Uncontrolled"


def can_have_support(sp):
    return not is_loc(sp) and sp["population"] > 0


def support_value(sp):
    if not can_have_support(sp):
        return 0
    return {"Passive Support": sp["population"], "Active Support": 2 * sp["population"]}.get(sp["support"], 0)


def opposition_value(sp):
    if not can_have_support(sp):
        return 0
    return {"Passive Opposition": sp["population"], "Active Opposition": 2 * sp["population"]}.get(sp["support"], 0)


def bases_on_map(state, faction):
    return sum(1 for sp in state["spaces"] for n in sp["pieces"]
               if PIECE_INFO[n][0] == faction and PIECE_INFO[n][1] == "Bases")


def scores(state):
    sp_list = state["spaces"]
    total_support = sum(support_value(s) for s in sp_list)
    total_opp = sum(opposition_value(s) for s in sp_list)
    coin_ctrl = sum(s["population"] for s in sp_list if control(s) == "COIN Control")
    nva_ctrl = sum(s["population"] for s in sp_list if control(s) == "NVA Control")
    av = available(state)
    us_avail = av["US"]["Troops"] + av["US"]["Bases"]
    points = {
        "US": total_support + us_avail,
        "ARVN": coin_ctrl + state["patronage"],
        "NVA": nva_ctrl + bases_on_map(state, "NVA"),
        "VC": total_opp + bases_on_map(state, "VC"),
    }
    detail = {
        "US": f"Total Support {total_support} + US Troops/Bases Available {us_avail}",
        "ARVN": f"COIN Control {coin_ctrl} + Patronage {state['patronage']}",
        "NVA": f"NVA Control {nva_ctrl} + NVA Bases on map {bases_on_map(state, 'NVA')}",
        "VC": f"Total Opposition {total_opp} + VC Bases on map {bases_on_map(state, 'VC')}",
    }
    result = {}
    for f in FACTIONS:
        result[f] = {"points": points[f], "threshold": THRESHOLDS[f],
                     "score": points[f] - THRESHOLDS[f], "detail": detail[f]}
    return result


def ranked(sc):
    """Victory ranking: highest score first, ties broken VC, ARVN, NVA, US."""
    return sorted(FACTIONS, key=lambda f: (-sc[f]["score"], TIE_ORDER.index(f)))


def space_map(state):
    return {sp["name"]: sp for sp in state["spaces"]}


def region_of(name):
    for reg, names in REGIONS:
        if name in names:
            return reg
    return "Other"


def card_line(cards, num, with_text=True):
    c = cards.get(str(num))
    if not c:
        return f"#{num} (unknown card)"
    head = f"#{num} {c['title']}"
    if c["type"] == "coup":
        return f"{head} [COUP]" + (f" Leader effect: {c['leaderEffect']}" if with_text and c.get("leaderEffect") else "")
    order = ", ".join(c["factionOrder"])
    marks = "; ".join(f"{f} {v['priority']}/{v['side']}" for f, v in c["botPriorities"].items() if f != "US")
    lines = [f"{head} (order: {order})"]
    if c["type"] == "pivotal":
        lines[0] += f" [{c['pivotalFaction']} PIVOTAL]"
    lines.append(f"    Tru'ng markings: {marks}")
    if with_text:
        if c["type"] == "dual":
            lines.append(f"    Unshaded: {c['unshaded']}")
            lines.append(f"    Shaded:   {c['shaded']}")
        elif c["type"] == "pivotal":
            lines.append(f"    Condition: {c['pivotalCondition']}")
            lines.append(f"    Text: {c['text']}")
        else:
            lines.append(f"    Text: {c['text']}")
        if c.get("momentum"):
            lines.append("    (MOMENTUM: lasting effect until the next Coup round)")
    return "\n".join(lines)
