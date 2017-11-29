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


print_age("john", 15

def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))
# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
elif percentage < 90 and percentage >=80 :
        return "B"
elif percentage >= 70 :
        return "C"
elif percentage >= 60 :
         return "D"