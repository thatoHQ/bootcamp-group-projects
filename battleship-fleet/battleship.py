COLUMNS = "ABCDEFGHIJ"
ROWS = range(1, 11)

BOARD_CELLS = [f"{column}{row}" for column in COLUMNS for row in ROWS]

FLEET = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2,
}


def parse_state(text):
    ships_str, shots_str = [part.strip() for part in text.split("|")]

    ships = {}
    for entry in ships_str.split(";"):
        name, cells = entry.split(":")
        ships[name.strip()] = [cell.strip() for cell in cells.split(",")]

    shots = [cell.strip() for cell in shots_str.split(",") if cell.strip()]

    return ...


def generate_legal_shots(state):
    raise NotImplementedError("This function is not implemented yet.")


def apply_shot(state, cell):
    raise NotImplementedError("This function is not implemented yet.")

def generate_legal_shots(state):
    legal_shots = []
    for cell in BOARD_CELLS:
        if cell not in state["shots"]:
            legal_shots.append(cell)
    return legal_shots

def apply(state, cell):
    if cell in state["shots"]:
        raise ValueError("Already fired at this cell")
    
    if cell not in BOARD_CELLS:
        raise ValueError("Cell is off the board")
    
    state["shots"].append(cell)
    hit_ship = None
