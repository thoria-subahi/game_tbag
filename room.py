class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.items = []
        self.character = None

    #creating getter and setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    def describe(self):
        print(self.description)


    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link #setting a key value pair (direction is a key), room_to_link is value..

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to the {self.name}")

    def get_details(self, player_inventory):
        print(f"\nRight now you are in the {self.name}")
        print("-------------------------")
        print(self.description)

        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")
        if self.items:
            print("\nItems in the room:")
            for item in self.items:
                print(f"{item.name}: {item.description}")
        if self.character:
            print(f"\nThere is someone here: {self.character.name}")
            

        
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You are forbidden from entering through this path!")
            return self

   