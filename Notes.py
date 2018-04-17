""""
import random # this should be on line
# # This is working
# print("hello world")
#
# # Doua Vue
# # (this is python 2.7)
#
# print(3+5)
# print(5-3)
# print(3*5)
# print(6/2)
# print(3** 2)
#
# print # this makes a new line. In python 3.6, it look like: print()
# print("see if you can figure this out")
# print(13 % 12)
#
# car_name= "Doua Vue"
# car_type= "tesla"
# car_cylinders= 8
# car_mpg = 9000.1
#
# # Inline car
# print("I have a car called the %s" % car_name)
# print("I have a car called the %s. It's a %s." % car_name, car_type)
# # asking for unput
# name = input("what is your name")# In the python
# print ("")
#

#functions


def print_hw():
    print("hello world")


print_hw()
print_hw()
print_hw()


def say_hi(name): # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("John")


def print_age(name,age):
    print("%s is %d years old." %(name, age))
    age += 1 # age = age + 1
    print("next year, they will be %d" % age)


print_age("john", 15)

def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))
# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage < 90 and percentage>= 90 :
        return "B"
    elif percentage >=90 :
        return "C"

'''Write a Function called "happy_bday"
that "sings" (prints) Happy birthday

It must take one parameter called "name" 
'''

def happy_bday(name):
    print("happy birthday to you" + ",")
    print("happy birthday to you" + ",")
    print("happy birthday to " + name + ",")
    print("happy birthday to you" + ".")

happy_bday("john")


# loops

for num in range(10):
    print(num + 1)

# DO NOT RUN!!!!!!!
a = 1
while a <= 10:
    print (a)
    a += 1

# random Number

print (random.randint(0,100))


# Lists

the_count = [ 1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls","Milk", "Soda","Chips"]

print(len(shopping_list))

# Going through a list
print(shopping_list[0])
print(shopping_list[2])

for item in shopping_list:
    print(item)

for num in the_count:
    print(num)

for num in the_count:
    print(num * 2)

len(shopping_list) # Give me the length of the list
range(3) # Give a list of the number 0 through 2
range(len(shopping_list)) # a list of every index a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("the item at index %d is %s" % (num, item))

# turn things into a list
str1 = "hello class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

#add things to a list
shopping_list.add("cereal")
print(shopping_list)

shopping_list.add("lemon")
print(shopping_list)

# removing things from a list
shopping_list.remove("soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

#dealing with strings
strTwo = "ThIs Is a VeRY oDd sEnTenCe"
lowercase = strTwo.lower()
"""

#Dictionaries - made up of key: Value Pairs
dictionary = {'name':'Lance','age': 23,'height': 5 * 12 + 7}

# Accessing Dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

#Adding to a dictionary
dictionary['weight'] = 280
print(dictionary)

large_dictionary = {
    'CA':'California',
    'FL':'Florida',
    'OH':'Ohio'
}

print(large_dictionary['FL'])

larger_dictionary = {
    'CA':[
        'Fresno',
        'Sacramento',
        'Los Angeles'
    ],
    'FL':[
        "tampa",
        "Orlando",
        "Miami"
    ],
    'OH':[
        "cleavland",
        "cincinnati",
    ]
}

print(larger_dictionary['FL'])
print(larger_dictionary["FL"][2])

print(larger_dictionary["OH"][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

current_node = largest_dictionary['CA']
print(current_node)
print(current_node['POPULATION'])
print(current_node['NAME'])