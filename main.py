from room import Room #im importing (name of class)FROM (name of file)
from item import Item
from character import King, Princess, VillainQueen


player_inventory = []

dungeon = Room("Dungeon")
dungeon.description = "A scary room filled with rats and whispers echoing"

royal_chamber = Room("Royal Chamber")  
royal_chamber.description = "A bright room with a large throne and soft lights"

courtyard = Room("Courtyard")
courtyard.description = "A large outdoor space with a beautiful garden"

dungeon.link_room(royal_chamber, "north")
royal_chamber.link_room(dungeon, "south")
royal_chamber.link_room(courtyard, "east")
courtyard.link_room(royal_chamber, "west")

crystal_of_truth = Item("Crystal of Truth", "A glowing crystal that reveals lies.", "Reveals the villain queens deception.")
silver_cloak = Item("Silver Cloak", "A shimmering cloak that heals the wearer.", "Restores players health.")
dragon_sword = Item("Dragon Sword", "A legendary sword forged made from dragons teeth.", "Can defeat the villain queen.")

dungeon.add_item(crystal_of_truth)
royal_chamber.add_item(silver_cloak)
courtyard.add_item(dragon_sword)

king = King()
princess = Princess()
villain_queen = VillainQueen()

royal_chamber.set_character(king)
courtyard.set_character(princess)
dungeon.set_character(villain_queen)

current_room = royal_chamber

while True:
    current_room.get_details(player_inventory)
    action = input("\nWhat would you like to do? (move/talk/use item/quit): ").lower()

    if action == "move":
        direction = input("Where would you like to go? (north/east/south/west): ").lower()
        current_room = current_room.move(direction)

    elif action == "talk":
        character = current_room.get_character()
        if character:
            character.talk()
        else:
            print("There is no one to talk to.")
    
    elif action == "use item":
        if current_room.items:
            print("Items in this room: " + ", ".join(item.name for item in current_room.items))
            item_name = input("Which item would you like to use? ").strip()
            for item in current_room.items:
                if item.name.lower() == item_name.lower():
                    item.use_item()
                    if item.name == "Crystal of Truth" and isinstance(current_room.get_character(), VillainQueen):
                        print("You have successfully exposed the villain's lies! She has fled in fear!")
                        current_room.set_character(None)
                        print("Game Over! You have won!")
                        play_again = input("Do you want to play again? (yes/no): ").lower()
                        if play_again == "yes":
                            current_room = courtyard  
                            dungeon.set_character(villain_queen)
                            royal_chamber.set_character(king)
                            courtyard.set_character(princess)
                            player_inventory = []
                            break
                        else:
                            print("Thanks for playing!")
                            exit()
                    break
            else:
                print("That item is not here.")
        else:
            print("There are no items to use here.")

    elif action == "quit":
        print("Thanks for playing!")
        break

    else:
        print("ERROR. Please try again.")






