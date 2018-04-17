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


class rippedblackpant(Clothing):
    def __init__(self):
        super(rippedblackpant, self).__init__('Ripped_Black_Pant', 'A Pants', 'Black')

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
        self.healing = 20

    def healing(self):
        print("It's healing you by %s" % self.healing)


class Food(Consumable):
    def __init__(self):
        super(Food, self).__init__('Food', 'A Food')


class Water(Consumable):
    def __init__(self):
        super(Water, self).__init__('Water', 'H20')
