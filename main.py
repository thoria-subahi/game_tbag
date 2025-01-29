from room import Room #im importing Room (name of class)FROM room (name of file)

dungeon = Room("Dungeon")
dungeon.description = "A scary room filled with rats and monsters"

royal_chamber = Room("Royal Chamber")  
royal_chamber.description = "A bright room with a large throne and soft lights"

courtyard = Room("Courtyard")
courtyard.description = "A large outdoor space with a beautiful garden"

dungeon.link_room(royal_chamber, "north")
royal_chamber.link_room(dungeon, "south")

royal_chamber.link_room(courtyard, "east")
courtyard.link_room(royal_chamber, "west")

dungeon.get_details()
royal_chamber.get_details()
courtyard.get_details()



