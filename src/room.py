# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []

    def print_items(self):
        if len(self.items) > 0:
            room_items = "\n".join([str(item) for item in self.items])
        else:
            room_items = "empty room"
        print(f"A {room_items} is visible")
