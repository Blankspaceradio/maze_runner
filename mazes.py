import random




ROOM_TYPES = [
    {"Left": None, "Right": None, "Forward": None, "Back": None},
    {"Left": None, "Forward": None, "Back": None},
    {"Left": None, "Right": None, "Back": None},
    {"Forward": None, "Right": None, "Back": None},
    {"Left": None, "Back": None},
    {"Forward": None, "Back": None},
    {"Right": None, "Back": None},
    {"Back": None},
]

OPPOSITE = {
    "Left": "Right",
    "Right": "Left",
    "Forward": "Back",
    "Back": "Forward",
}


def generate_maze():
    room_selector = random.choice(ROOM_TYPES)
    return room_selector


def generate_room():
    return random.choice(ROOM_TYPES)


