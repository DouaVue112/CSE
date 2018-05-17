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
        print("Can help you from getting bit from snake or any type of animal but not really ")


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
        self.healing = 10

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


Guy = Character("Name: Jimmy", "Health: 20%", [Cap], "Clothing: Style Clothing", "Description: You are smart "
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
vans = Vans('vans')
goldenwatch = GoldenWatch()
food = Food()
water = Water()


class Balance(object):
    def __init__(self, money):
        self.Money = 20


Dude = Balance("Balance: 20")
print(Dude.Money)


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


House = Room("House", "There is 20 dollars and a bank card on the table. Also a ripped black pants "
                      "and a pair of vans in your dressing room."
                      " You must eat about 8 types of food from some Fast Food stores"
                      " to get full. "
                      "A door leads to east.", None, None, 'Down_Town', None,
             [BankCard, Cap, Vans, RippedBlackPant])
Down_Town = Room("Down Town", "Now you are in down town and you found a spirit knife. A street leads north to "
                              "the food places.", 'Pizza_Huts',
                 None, None, None, SpiritKnife)
Pizza_Huts = Room("Pizza Huts", "Your first stop is at Pizza Hut. You have wasted 5 dollars on the largest pizza but "
                                "you're still very hungry. "
                                "The Pizza H"
                                "ut gave you a Supreme Jacket because you ate "
                                "the biggest pizza that they had. Go to the next stop."
                                "", 'Taco_Bell', None, None, None, SupremeJacket)
Taco_Bell = Room("Taco Bell", "You again wasted 5 dollars at Taco Bell. You have ate two types of food. "
                              "Go west to eat more.",
                 None, None, None, 'Burger_Kings', None)
Burger_Kings = Room("Burger Kings", "You now ate a burger and the burger was 5 dollars."
                                    " You now ate 3 types of food.", None, None, None, 'Subway', None)
Subway = Room("Subway", "You then ate a sandwich and you were looking "
                        "for more money. You searched and searched but your pockets "
                        "didn't have any money at all. "
                        "You also dropped the spirit knife but you remember you still got your bank card "
                        "to go get more money. "
                        "There is a bank south and west.",
              None, 'Bank_South', None, 'Bank_West', None)
Bank_West = Room("Bank West", "You are at bank west. You took out 40 dollars. On your way there, "
                              "you saw two McDonald's.",
                 'North_McDonald', 'South_McDonald', None, None, None)
Bank_South = Room("Bank South", "You took out 10 dollars in your bank. A east KFC leads east.",
                  None, None, 'East_KFC', None, None)
North_McDonald = Room("North McDonald", "They ripped you off. The meal was 10 dollars. A street leads to east."
                                        " You have 30 dollars now and ate 5 types of food.", None, None, 'Forest',
                      None, Water)
Forest = Room("Forest", "You are now in the forest. There is no one around you and you're confused on where to go. "
                        "You see two ways into the light but there's is only one way out and the other is death."
                        " North or East???", 'Ghost',
              None, 'People', None, None)
South_McDonald = Room("South McDonald", "You order your food. It costs 5 dollars. After from all that "
                                        "eating your still very hungry. Now you"
                                        " already ate 5 types of food and also asked for water to help you on your way"
                                        " to the next Fast Food stores.",
                                        None, None, 'South_KFC', None, Water)
Ghost = Room("Ghost", "The ghost is wearing a white dress with lots and lots of blood all over it's dress. "
                      "She have a long black hair and she looked at you with her long tongue out with her neck turned."
                      "It scared you to death. Sadly,"
                      " You Have Died!!!!!!!!!!", None, None, None, None, None)
People = Room("People", "You see people. You asked for help. "
                        "They told you to go south and gave you a golden watch to help you the way to food max. "
                        "The golden watch can tell time and give directions.", None,
              'Food_Max', None, None, GoldenWatch)
South_KFC = Room("South KFC", "You ate some KFC. You wasted a 5 dollar meal and now you have ate 6 types of foods."
                              "", 'In_N_Out', None, None, None, None)
Food_Max = Room("Food Max", "You have wasted 20 dollars on drinks. Now you only have 10 dollars but your still hungry."
                            " You can go to the east KFC or your friends house. You choose."
                            "", None, 'Friends_House', 'East_KFC', None, Food)
In_N_Out = Room("In N Out", "You bought a 5 dollar meal. The 5 dollar meal was a burger and fries with a drink. "
                            "After eating that big burger and fries your still hungry. Go north.", 'Starbucks',
                None, None,
                None, None)
Starbucks = Room("Starbucks", "Finally, your at starbucks and you got a vanilla bean frappuccino and it tasted amazing."
                              "But!!!!!! Guess What!! Your full now. You can go home."
                              " Go West to House.", None, None, None, 'Back_To_House', None)
East_KFC = Room("East KFC", "You bought a food for 10 dollars. "
                            "You have no more money to go home or anywhere else and the banks are too "
                            "far for you to go to. "
                            "You Lost!!!!!!! Thanks!! For!! Playing!!", None, None, None,
                None, None)
Friends_House = Room("Friends House", "Your friend bought a lot of pizza and lots of soda. "
                                      "He told you to eat the pizza with him. "
                                      "Now you got full and your able to save 10 dollars. It's time"
                                      " for you to go home and rest. Go West to your house.", None, None, None,
                     'Back_To_House', None)
Back_To_House = Room("Back To House", "You are home now, rest up and THANK YOU!!!!!!! COME AGAIN!!!!", None,
                     None, None, None, None)

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
    if command == 'inv':
        print(Guy.inventory)

    if current_node == Back_To_House:
        print(Back_To_House.name)
        print(Back_To_House.description)
        exit(0)

    if current_node == Ghost:
        print(Ghost.name)
        print(Ghost.description)
        exit(0)

    if current_node == East_KFC:
        print(East_KFC.name)
        print(East_KFC.description)
        exit(0)

    elif command == 'Take clothing':
        if current_node.Clothing is not None:
            Guy.add_Clothing(current_node.Clothing)
            current_node.Clothing = None
        else:
            print("There is no clothing here")
    elif command == 'Take':
        Item.name = input('Take what?')
        found = False
        if current_node.Item is not None:
            for item in current_node.Item:
                if Item == Item.name:
                    print("Taken")
                    Guy.inventory.append(item)
                    found = True
        if not found:
            print("It isn't here")
