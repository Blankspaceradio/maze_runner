from mazes import *
from rooms import *

def main():
    finished = False
    maze = {0:{"Left": None, "Right": None, "Forward": None}}
    room_id = 0
    next_step = False
    while next_step == False:
        print("ENTRANCE")
        show_room(maze[0])
        users_choice = input().capitalize()
        print()
        next_step = go_to_next_room(maze, room_id, users_choice)


    while finished == False:
        next_step = False
        if users_choice != "Back":
            room = generate_maze()
            room_id += 1
            maze[room_id] = room
            while next_step == False:
                print(f"ROOM {room_id}")
                show_room(room)
                users_choice = input().capitalize()
                print()
                next_step = go_to_next_room(maze, room_id, users_choice)
                
        else:
            room_id -= 1
            pervious_room = maze[room_id]
            while next_step == False:
                if room_id == 0:
                    print("ENTRANCE")
                else:
                    print(f"ROOM {room_id}:")
                show_room(pervious_room)
                users_choice = input().capitalize()
                print()
                next_step = go_to_next_room(maze, room_id, users_choice)


if __name__ == "__main__":
    main()