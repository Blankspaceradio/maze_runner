


def show_room(room):
    if len(room) == 1:
        print("Dead End.")
    print("You can go:")
    for i in room:
        print(f"- {i}")
    print("Which direction do you go?")

def go_to_next_room(maze, room_id, users_choice):
    if users_choice not in maze[room_id]:
        print("You can't go that way.")
        print()
        return False
    else:
        return True
