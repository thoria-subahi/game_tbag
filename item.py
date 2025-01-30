class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use_item(self):
        print(f"You have used the {self.name}. {self.effect}")
