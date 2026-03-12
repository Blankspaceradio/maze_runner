import random

ITEMS = ["Gold", "Sword", "Spear", "Jug of Water", "Sheild", "Potion"]
inventory = {}

def generate_item():
    ran_item = random.choice(ITEMS)
    if ran_item == "Gold":
        amount =  random.randint(1, 25)
    else:
        amount = random.randint(1, 3)
    add_item(ran_item, amount)
    display_item(ran_item,amount)

def add_item(item, amount):
    if item in inventory:
        inventory[item] = amount
    else:
        inventory[item] = amount

def display_item(item, amount):
    print("")
    print(f"you found {amount} {item}")

def display_inventory():
    print("")
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"- {item}: {quantity}")