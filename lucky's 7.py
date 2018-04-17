import random

Money_left = 15
play = 0
while Money_left > 0 :
    D1 = (random.randint(1, 6))
    D2 = (random.randint(1, 6))
    roll = (D1 + D2)
    play += 1

    if D1+D2 == 7:
        print ()
        Money_left += 4







