from mazes import *
from rooms import *

def main():
    finished = False
    maze = {0:{"Left": None, "Right": None, "Forward": None}}
    current_room = 0
        
    while finished == False:
        show_map(maze, current_room)
        show_room(maze[current_room])
        direction = input().capitalize()

        if direction not in maze[current_room]:
            print("You can't go that way")
            continue
        if maze[current_room][direction] is None:
            new_room_id = new_room(maze, current_room, direction)
            current_room = new_room_id
        else:
            current_room = maze[current_room][direction]

if __name__ == "__main__":
    main()