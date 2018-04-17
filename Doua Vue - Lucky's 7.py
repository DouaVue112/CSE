import random

round = 0
Money_left = 15
left_over_money = 0
Most_Money = Money_left
Highest_Round = 0

while Money_left > 0 :
    D1 = (random.randint(1, 6))
    D2 = (random.randint(1, 6))
    roll = (D1 + D2)
    round += 1
    print(roll)

    if (roll) == 7:
        print("You win 4 Dollars")
        Money_left += 4

        if Money_left > Most_Money:
            Most_Money = Money_left
            Highest_Round = round

    else:
        print("You Lose 1 Dollars")
        Money_left -= 1

    print("You have $%s." % Money_left)

print("You lost all your money.")
print("You did %s round" % round)
print("The most money you has was $%s" % Most_Money)
print("You should of stopped at round %s." % Highest_Round)
