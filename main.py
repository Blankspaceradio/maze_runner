from mazes import *


def main():
    finished = False
    maze = {0:["Left", "Right", "Forward"]}
    room_id = 0
    for item in maze[0]:
        print(item)
    print("Which direction do you go?")
    users_choice = input()
    print()
    if users_choice not in maze[0]:
        print("You can't go that way.")


    while finished == False:
        if users_choice != "Back":
            room = generate_maze()
            room_id += 1
            maze[room_id] = room
            for choice in room:
                if len(room) == 1:
                    print("Dead End.")
                    print(choice)
                else:
                    print(choice)
            print("Which direction do you go?")
            users_choice = input()
            print()
        else:
            finished = True


if __name__ == "__main__":
    main()