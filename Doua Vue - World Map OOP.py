class Room(object):
    def __init__(self, name, description, north, south, east, west):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
House = Room("House", "There is 20 dollars on the table. You must eat about 8 type of food to get full. "
                      "A door lead east.", None, None, 'Down_Town', None)
Down_Town = Room("Down Town", "Now you are in down town. A street leads north to the food places.", 'Pizza_Huts',
                 None, None, None)
Pizza_Huts = Room("Pizza Huts", "You have wasted 5 dollars on a pizza but your still hungry."
                                "There is a taco bell North.", 'Taco_Bell', None, None, None)
Taco_Bell = Room("Taco Bell", "You again waste 5 dollars. You have ate two type of food. Go west for burger king.",
                 None, None, None, 'Burger_Kings')
Burger_Kings = Room("Burger Kings", "You now ate a burger and the burger was 5 dollars."
                                    "You ate 3 types of food. Go west.", None, None, None, 'Subway')
Subway = Room("Subway", "You now ate a sandwich and is out of money. There is a bank south and west.",
              None, 'Bank_South', None, 'Bank_West')
Bank_West = Room("Bank West", "You are at bank west. You took out 40 dollars.A McDonald is North and South.",
                 'North_McDonald', 'South_McDonald', None, None)
Bank_South = Room("Bank South", "You took out 10 dollars in your bank. A east KFC leads east.",
                  None, None, 'East_KFC', None)
North_McDonald = Room("North McDonald", "They riped you off. The meal was 10 dollars. A street lead east."
                                        "You have 30 dollars now and ate 5 types of food.", None, None, 'Forest', None)
Forest = Room("Forest", "You are now in the forest. There's is only one ways out. North or East.", 'Ghost',
              None, 'People', None)
South_McDonald = Room("South McDonald", "You order your food. It cost 5 dollars. You still need to east but now you"
                                        "already ate 5 food.", None, None, 'South_KFC', None)
Ghost = Room("Ghost", "The ghost is wearing a white dress with blood all over its dress. It scared you to death. Sadly,"
                      " You Have Die.", None, None, None, None)
People = Room("People", "You see people. You asked for help. They told you to go south to go to a food max.", None,
              'Food_Max', None, None)
South_KFC = Room("South KFC", "You ate some KFC. You wasted a 5 dollars meal and now you have ate 6 foods."
                              " A In N Out is north.", 'In_N_Out', None, None, None)
Food_Max = Room("Food Max", "You have wasted 20 dollars on drinks. Now you only have 10 dollars but your still hungry."
                            " A east KFC is east or you can go to your friends house south."
                            "", None, 'Friends_House', 'East_KfC', None)
In_N_Out = Room("In N Out", "You bought a 5 dollars meal. Your still hungry. Go north.", 'Starbucks', None, None, None)
Starbucks = Room("Starbucks", "Finally, You got full. Go West to House.", None, None, None, 'Back_To_House')
East_KFC = Room("East KFC", "You bought a food for 10 dollars. "
                            "You have no more money to go home. You Lost!!!!!!!", None, None, None, None)
Friends_House = Room("Friends House", "Your friend bought a pizza. He told chu to eat. Now you got full and it's time"
                                      " for you to go home and rest. Go West to House."
                                      , None, None, None, 'Back_To_House')
Back_To_House = Room("Back To House", "You are home now, rest up and thanks for playing.", None, None, None, None)

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
