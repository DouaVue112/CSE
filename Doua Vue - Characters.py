class Character(object):
    def __init__(self, name, health, inventory, clothes, description):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.clothes = clothes
        self.description = description
        self.move = True
        self.pick = True

    def Move_Forward(self):
        if self.move:
            print("You moved")
        else:
            print("Nothing happen")

    def Pick_Up(self):
        if self.pick:
            print("You picked up an item")
        else:
            print("You can't pick up that item")


Guy = Character("Jimmy", "0%", "Money", "Style Clothing", "You are smart and love to play video games and"
                                                          " sport but most of all, you get hungry a lot")

print(Guy.name)
print(Guy.health)
print(Guy.clothes)
print(Guy.description)