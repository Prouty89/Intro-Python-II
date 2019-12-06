from room import Room
from player import Player
from item import Item

items = {
    "sword": Item("sword", "a sharp sword"),
    "candle": Item("torch", "a burning candle"),
    "chest": Item("chest", "a treasure test"),
    "key": Item("key", "a rusty key"),
    "bomb": Item("map", "a treasure map"),
}

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].items.append('sword')
room['foyer'].items.append('map')
room['overlook'].items.append('key')
room['narrow'].items.append('torch')
room['treasure'].items.append('chest')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Input player name: ')
player = Player(name, room["outside"])
print("\n===============")
print(f"Welcome, {player.name}!")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
choice = None
moved = True
while choice not in ['q', 'quit']:
    print("===============\n")
    print(f"{player.name} in \"{player.room.name}\"")
    print(f"{player.room.desc}\n")
    player.room.print_items()

    choice = input(
        "\nCheck Inventory (i/inv), Move (n, s, w, e) or Grab an Item (add/drop): ")
    choice_arr = choice.split(' ')
    choice_len = len(choice_arr)

    if moved:
        if choice in ['n', 'N'] and hasattr(player.room, 'n_to'):
            player.room = player.room.n_to
        elif choice in ['s', 'S'] and hasattr(player.room, 's_to'):
            player.room = player.room.s_to
        elif choice in ['e', 'E'] and hasattr(player.room, 'e_to'):
            player.room = player.room.e_to
        elif choice in ['w', 'W'] and hasattr(player.room, 'w_to'):
            player.room = player.room.w_to
        elif choice in ['i', 'inv']:
            player.inventory()
        elif choice in ['q', 'quit']:
            print(f"\nThanks for playing!\n")
            moved = False
        else:
            print(
                f"\n!*****!\nMove not allowed, please select again\n!*****!\n")

    if choice_len == 2:
        action = choice_arr[0]
        item = choice_arr[1]
        if action in ['add']:
            if item in items.keys() and items[item] in player.room.items:
                player.add_item(items[item])
                print(f"{player.name} picks up a {item}!\n")
            else:
                print(f"This isn't available to pick up.\n")
        if action == 'drop':
            if item in items.keys() and items[item] in player.items:
                player.drop_item(items[item])
                print(f"{player.name} drops {item}.\n")
            else:
                print(f"You don't have an item to drop.\n")
