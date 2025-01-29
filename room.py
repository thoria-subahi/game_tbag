class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

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


    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")
    