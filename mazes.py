import random
from items import *



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
    room_selector = random.choice(ROOM_TYPES).copy()
    return room_selector


def new_room(maze, room_id, users_choice):
    if random.random() < 0.2:
        new_room = random.choice(list(maze.keys()))
    else:
        new_room = len(maze)
        maze[new_room] = generate_maze()
        connect(maze, room_id, users_choice, new_room)
        if random.random() < 0.8:
            generate_item()
        else:
            print("")
            print("No items found")
    return new_room


def connect(maze,current_room, choice, new_room):

    maze[current_room][choice] = new_room
    opposite = OPPOSITE[choice]
    if opposite not in maze[new_room]:
        maze[new_room][opposite] = None
    maze[new_room][opposite] = current_room

def show_map(maze, current_room):

    print("\n--- MAP ---")

    for room, paths in maze.items():

        marker = " <YOU>" if room == current_room else ""

        print(f"{room}: {paths}{marker}")

    print("-----------\n")