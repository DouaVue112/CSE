class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def name(self):
        print("You have a %s" % self.name)

    def description(self):
        print("Your item is useful for a reason in the game")


class Weapon(Item):
    def __init__(self, name, description, skill, ):
        super(Weapon, self).__init__(name, description)
        self.skill = skill

    def skill(self):
        print("Your skill of your weapon is to %s" % self.skill)


class SpiritKnife(Weapon):
    def __init__(self):
        super(SpiritKnife, self).__init__('Spirit_Knife', 'A Knife that can kill ghost or evil things', 'To defend')

    def slice(self):
        print("For every time you slice, lighting and wind come out of your knife to kill an ghost or evil things")


class Card(Item):
    def __init__(self, name, description):
        super(Card, self).__init__(name, description)
        self.amount = 60

    def place(self):
        print("The place of two ATM's are at Bank West and Bank South")

    def amount(self):
        print("You have about %s$ in my bank" % self.amount)


class BankCard(Card):
    def __init__(self):
        super(BankCard, self).__init__('Bank_Card', 'A Card That Have Money')

    def moremoney(self):
        print("This card give you more money then you are suppose to get")


class Clothing(Item):
    def __init__(self, name, description, color):
        super(Clothing, self).__init__(name, description)
        self.color = color

    def color(self):
        print("Your Clothing is this %s" % self.color)


class Cap(Clothing):
    def __init__(self):
        super(Cap, self).__init__('Cap', 'A Hat', 'White')

    def coverhead(self):
        print("Your Cap is like a helmet")


class SupremeJacket(Clothing):
    def __init__(self):
        super(SupremeJacket, self).__init__('Supreme_Jacket', 'A Jacket', 'red')

    def armor(self):
        print("You Jacket is like armor but not really")


class RippedBlackPant(Clothing):
    def __init__(self):
        super(RippedBlackPant, self).__init__('Ripped_Black_Pant', 'A Pants', 'Black')

    def pantarmor(self):
        print("Can help you from getting bit from snake or any type of anime but not really ")


class Vans(Clothing):
    def __init__(self, shoes):
        super(Vans, self).__init__('Vans', 'A shoes', 'White')
        self.shoes = shoes

    def shoes(self):
        print("Your vans are %s" % self.shoes)


class Time(Item):
    def __init__(self, name, description):
        super(Time, self).__init__(name, description)

    def keepup(self):
        print("Help you keep up with the time")


class GoldenWatch(Time):
    def __init__(self):
        super(GoldenWatch, self).__init__('Golden_Watch', 'A watch')


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)
        self.healing = 20

    def healing(self):
        print("It's healing you by %s" % self.healing)


class Food(Consumable):
    def __init__(self):
        super(Food, self).__init__('Food', 'A Food')


class Water(Consumable):
    def __init__(self):
        super(Water, self).__init__('Water', 'H20')


class Character(object):
    def __init__(self, name, health, inventory, clothes, description):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.clothes = clothes
        self.description = description
        self.move = True
        self.pick = True

    def moveforward(self):
        if self.move:
            print("You moved")
        else:
            print("Nothing happen")

    def pickup(self):
        if self.pick:
            print("You picked up an item")
        else:
            print("You can't pick up that item")


Guy = Character("Name: Jimmy", "Health: 0%", "Money", "Clothing: Style Clothing", "Description: You are smart "
                                                                                  "and love to "
                                                                                  "play video games and"
                                                                                  " sport but most of all, "
                                                                                  "you get hungry a lot")
print(Guy.name)
print(Guy.health)
print(Guy.clothes)
print(Guy.description)

spiritknife = SpiritKnife()
bankcard = BankCard()
cap = Cap()
supremejacket = SupremeJacket()
rippedblackpant = RippedBlackPant()
vans = Vans('Shoes')
goldenwatch = GoldenWatch()
food = Food()
water = Water()


class Room(object):
    def __init__(self, name, description, north, south, east, west, item):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
House = Room("House", "There is 20 dollars on the table. You must eat about 8 type of food to get full. "
                      "A door lead east.", None, None, 'Down_Town', None,
             ['Bank Card', 'Cap', 'Vans', 'Ripped Black Pant'])
Down_Town = Room("Down Town", "Now you are in down town and you found a spirit knife. A street leads north to "
                              "the food places.", 'Pizza_Huts',
                 None, None, None, 'Spirit Knife')
Pizza_Huts = Room("Pizza Huts", "You have wasted 5 dollars on the largest pizza but your still hungry. "
                                "The Pizza Hut gave you a Supreme Jacket because you ate "
                                "the biggest pizza that they had."
                                "There is a taco bell North.", 'Taco_Bell', None, None, None, 'Supreme Jacket')
Taco_Bell = Room("Taco Bell", "You again waste 5 dollars. You have ate two type of food. Go west for burger king.",
                 None, None, None, 'Burger_Kings', None)
Burger_Kings = Room("Burger Kings", "You now ate a burger and the burger was 5 dollars."
                                    "You ate 3 types of food. Go west.", None, None, None, 'Subway', None)
Subway = Room("Subway", "You now ate a sandwich and was looking for more money. You search and search but your pockets "
                        "didn't have many money. "
                        "You then dropped the spirit knife but you still got your bank card to go get more money. "
                        "There is a bank south and west.",
              None, 'Bank_South', None, 'Bank_West', None)
Bank_West = Room("Bank West", "You are at bank west. You took out 40 dollars.A McDonald is North and South.",
                 'North_McDonald', 'South_McDonald', None, None, None)
Bank_South = Room("Bank South", "You took out 10 dollars in your bank. A east KFC leads east.",
                  None, None, 'East_KFC', None, None)
North_McDonald = Room("North McDonald", "They riped you off. The meal was 10 dollars. A street lead east."
                                        "You have 30 dollars now and ate 5 types of food.", None, None, 'Forest',
                      None, 'Water')
Forest = Room("Forest", "You are now in the forest. There is no one around you and your confused on where to go. "
                        "You see two ways into the light but there's is only one ways out. North or East.", 'Ghost',
              None, 'People', None, None)
South_McDonald = Room("South McDonald", "You order your food. It cost 5 dollars. You still need to east but now you"
                                        "already ate 5 food and asked for water to help you on your way east",
                      None, None, 'South_KFC', None, 'Water')
Ghost = Room("Ghost", "The ghost is wearing a white dress with blood all over its dress. It scared you to death. Sadly,"
                      " You Have Died.", None, None, None, None, None)
People = Room("People", "You see people. You asked for help. "
                        "They told you to go south and gave you a golden watch to help you the way to food max. "
                        "The golden watch can tell time and give directions.", None,
              'Food_Max', None, None, 'Golden Watch')
South_KFC = Room("South KFC", "You ate some KFC. You wasted a 5 dollars meal and now you have ate 6 foods."
                              " A In N Out is north.", 'In_N_Out', None, None, None, None)
Food_Max = Room("Food Max", "You have wasted 20 dollars on drinks. Now you only have 10 dollars but your still hungry."
                            " A east KFC is east or you can go to your friends house south."
                            "", None, 'Friends_House', 'East_KfC', None, 'Food')
In_N_Out = Room("In N Out", "You bought a 5 dollars meal. Your still hungry. Go north.", 'Starbucks', None, None,
                None, None)
Starbucks = Room("Starbucks", "Finally, You got full. Go West to House.", None, None, None, 'Back_To_House', None)
East_KFC = Room("East KFC", "You bought a food for 10 dollars. "
                            "You have no more money to go home. You Lost!!!!!!!", None, None, None, None, None)
Friends_House = Room("Friends House", "Your friend bought a pizza. He told chu to eat. Now you got full and it's time"
                                      " for you to go home and rest. Go West to your house.", None, None, None,
                     'Back_To_House', None)
Back_To_House = Room("Back To House", "You are home now, rest up and thanks for playing.", None, None, None, None, None)

current_node = House
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print('Command Not Recognized')
