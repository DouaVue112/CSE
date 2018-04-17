world_map = {
    'HOUSE': {
        'NAME': "House",
        'DESCRIPTION': "There is 20 dollars on the table. You must eat about 8 type of food to get full. "
                       "A door lead east.",
        'PATHS': {
            'EAST': 'DOWNTOWN'
        }
    },
    "DOWNTOWN": {
        'NAME': "Down Town",
        'DESCRIPTION': "Now you are in down town. A street leads east to the food ideo. ",
        'PATHS': {
            'NORTH': 'PIZZA HUT'
        }
    },
    "PIZZA HUT": {
        'NAME': "Pizza Hut",
        'DESCRIPTION': "You have wasted 5 dollars on a pizza but your still hungry. There is a taco bell North.",
        'PATHS': {
            'NORTH': 'TACO BELL'
        }
    },
    "TACO BELL": {
        'NAME': "Taco Bell",
        'DESCRIPTION': "You again waste 5 dollars. You haved ate two type of food. Go west for burger king.",
        'PATHS': {
            'WEST': 'BURGER KINGS'
        }
    },
    "BURGER KINGS": {
        'NAME': "Burger Kings",
        'DESCRIPTION': "You now ate a burger and the burger was 5 dollars. You ate 3 types of food. Go west.",
        'PATHS': {
            'WEST': 'SUBWAY'
        }
    },
    "SUBWAY": {
        'NAME': "Subway",
        'DESCRIPTION': "You now ate a sandwich and is out of money. There is a bank south and west.",
        'PATHS': {
            'WEST': 'BANK WEST',
            'SOUTH': 'BANK SOUTH'
        }
    },
    "BANK WEST": {
        'NAME': "Bank West",
        'DESCRIPTION': "You are at bank west. You took out 40 dollars.A Mcdonald is North and South. ",
        'PATHS': {
            'NORTH': 'NORTH MCDONALD',
            'SOUTH': 'SOUTH MCDONALD'
        }

    },
    "BANK SOUTH": {
        'NAME': "Bank South",
        'DESCRIPTION': "You took out 20 dollars in your bank. A east KFC leads east.",
        'PATHS': {
            'EAST': 'EAST KFC'
        }
    },
    'NORTH MCDONALD': {
        'NAME': "North Mcdonalds",
        'DESRIPTION': "They riped you off. The meal was 10 dollars. "
                      "A street lead east.You have 30 dollars now and ate 5 types of food.",
        'PATHS': {
            'EAST': 'FOREST'
        }
    },
    'FOREST': {
        'NAME': "Forest",
        'DESCRIPTION': "You are now in the forest. There's is only one ways out. North or East.",
        'PATHS': {
            'NORTH': 'GHOST',
            'EAST': 'PEOPLE'
        }
    },
    'SOUTH MCDONALD': {
        'NAME': "South Mcdonald",
        'DESCRIPTION': "You order your food. It costed 5 dollars."
                       " You still need to east but now you already ate 5 food.",
        'PATHS': {
            'EAST': 'SOUTH KFC'
        }
    },
    'GHOST': {
        'NAME': "GHOST",
        'DESCRIPTION': "The ghost is wearing a white dress with blood all over its dress. "
                       "It scared you to death. Sadly,"
                       " You Have Die.",
        'PATHS': {
            exit(0)
        }
    },
    'PEOPLE': {
        'NAME': "People",
        'DESCIPTION': "You see people. You asked for help. They told you to go south to go to a food max. ",
        'PATHS': {
           'SOUTH': 'FOOD MAX'
        }
    },
    'SOUTH KFC': {
        'NAME': "South KFC",
        'DESCRIPTION': "You ate some KFC. You wasted a 5 dollars meal and now you have ate 6 foods. "
                       "A In N Out is north. ",
        'PATHS': {
            'NORTH': 'IN N OUT'
        }
    },
    'FOOD MAX': {
        'NAME': "Food Max",
        'DESCRIPTION': "You have wasted 20 dollars on drinks. Now you only have 10 dollars but your still hungry. "
                       "A east KFC is east or you can go to your friends house south. ",
        'PATHS': {
            'EAST': 'EAST KFC',
            'SOUTH': 'FRIENDS HOUSE'
        }
    },
    'IN N OUT': {
        'NAME': "In N Out",
        'DESCRIPTION': "You bought a 5 dollars meal. Your still hungry. Go north.",
        'PATHS': {
            'NORTH': 'STARBUCKS'
        }
    },
    'STARBUCKS': {
        'NAME': "Starbucks",
        'DESCRIPTION': "Finally, You got full. Go West to House.",
        'PATHS': {
            'WEST': 'HOUSE'
        }
    },
    'EAST KFC': {
        'NAME': "East KFC",
        'DESCRIPTION': "You bought a food for 10 dollars. You have no more money to go home. You Lost!!!!!!!",
        'PATHS': {
            exit(0)
        }
    },
    'FRIENDS HOUSE': {
        'NAME': "Friends House",
        'DECRYPTION': "Your friend bought a pizza. He told chu to eat. "
                      "Now you got full and it's time for you to go home and rest. Go West to House.",
        'PATHS': {
            'WEST': 'HOUSE'
        }
    }
}

current_node = world_map['HOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print('Command Not Recognized')

