class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation:
            print(f"{self.name} says '{self.conversation}' ")
        else:
            print(f"{self.name} doesn't want to say anything.")

    def describe(self):
        print(f"{self.name}: {self.description}")


class King(Character):
    def __init__(self, name="King", description="A kind and fair ruler."):
        super().__init__(name, description)
        self.set_conversation("Retrieve the Crystal of Truth to expose the villain queen!")

class Princess(Character):
    def __init__(self, name="Princess", description="A sweet and innocent soul."):
        super().__init__(name, description)
        self.set_conversation("Please help me escape the villain queen!")
    
    
class VillainQueen(Character):
    def __init__(self, name="Villain Queen", description="A powerful and evil queen."):
        super().__init__(name, description)
        self.set_conversation("You will never defeat me!")

  

