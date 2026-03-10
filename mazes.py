import random




ROOM_TYPES = [
    ["Left", "Right", "Forward", "Back"],
    ["Left", "Forward", "Back"],
    ["Left", "Right", "Back"],
    ["Forward", "Right", "Back"],
    ["Left", "Back"],
    ["Forward", "Back"],
    ["Right", "Back"],
    ["Back"]
]


def generate_maze():
    room_selector = random.choice(ROOM_TYPES)
    return room_selector
    
    



def generate_room():
    return random.choice(ROOM_TYPES)





