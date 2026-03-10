from mazes import *


def main():
    finished = False
    maze = {0:["Left", "Right", "Forward"]}
    room_id = 0
    next_step = False
    while next_step == False:
        print("ENTRANCE:")
        for item in maze[0]:
            print(item)
        print("Which direction do you go?")
        users_choice = input()
        print()
        if users_choice not in maze[0]:
            print("You can't go that way.")
            print()
            next_step = False
        else:
            next_step = True


    while finished == False:
        next_step = False
        if users_choice != "Back":
            room = generate_maze()
            room_id += 1
            maze[room_id] = room
            while next_step == False:
                print(f"ROOM {room_id}:")
                for choice in room:
                    if len(room) == 1:
                        print("Dead End.")
                        print(choice)
                    else:
                        print(choice)
                print("Which direction do you go?")
                users_choice = input()
                print()
                if users_choice not in maze[room_id]:
                    print("You can't go that way.")
                    print()
                    next_step = False
                else:
                    next_step = True
        else:
            room_id -= 1
            pervious_room = maze[room_id]
            while next_step == False:
                if room_id == 0:
                    print("ENTRANCE:")
                else:
                    print(f"ROOM {room_id}:")
                for choice in pervious_room:
                    if len(room) == 1:
                        print("Dead End.")
                        print(choice)
                    else:
                        print(choice)
                print("Which direction do you go?")
                users_choice = input()
                print()
                if users_choice not in maze[room_id]:
                    print("You can't go that way.")
                    print()
                    next_step = False
                else:
                    next_step = True


if __name__ == "__main__":
    main()