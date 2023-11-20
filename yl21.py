import random

x = random.randint(1, 100)

guess = int(input("paku number:"))

while True:
    if guess > x:
        print("arv on sellest väiksem")
    elif guess < x:
        print("arv on sellest suurem")
    else:
        print("arvasid õigesti!")
        break
    guess = int(input("paku number:"))
