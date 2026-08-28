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

##Thato
def parse_state(text):
    ships_str, shots_str = [part.strip() for part in text.split("|")]

    ships = {}
    for entry in ships_str.split(";"):
        name, cells = entry.split(":")
        ships[name.strip()] = [cell.strip() for cell in cells.split(",")]

    shots = [cell.strip() for cell in shots_str.split(",") if cell.strip()]

    return {"ships": ships, "shots": shots}



##Tumelo

def generate_legal_shots(state):
    legal_shots = []
    for cell in BOARD_CELLS:
        if cell not in state["shots"]:
            legal_shots.append(cell)
    return legal_shots




##Harry
def apply_shot(state, cell):
    if cell in state["shots"]:
        raise ValueError("Already fired at this cell")
    if cell not in BOARD_CELLS:
        raise ValueError("Cell is off the board")

    state["shots"].append(cell)
    hit_ship = None


#Nhluvuko
    for ship_name in state["ships"]:
        if cell in state["ships"][ship_name]:
            hit_ship = ship_name
            break  # Stop searching once we find the hit ship

    
    if hit_ship is None:
        result = "miss"
    else:
        is_sunk = True
        for c in state["ships"][hit_ship]:
            if c not in state["shots"]:
                is_sunk = False
                break 

        if is_sunk:
            result = "sunk:" + hit_ship
        else:
            result = "hit"





    # Thabiso
    fleet_defeated = True
    for ship_name in state["ships"]:
        for c in state["ships"][ship_name]:
            if c not in state["shots"]:
                fleet_defeated = False

    return {
        "state": state,
        "result": result,
        "fleet_defeated": fleet_defeated
    }

