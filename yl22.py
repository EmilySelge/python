import random

choices = ["kivi", "paber", "käärid"]
x = random.choice(choices)
u = input("kivi, paber, või käärid?")

while True:
    if u == "kivi" and x == "paber" or u == "paber" and x == "käärid" or u == "käärid" and x == "kivi":
        print("arvuti võitis")
        break
    elif u == "kivi" and x == "käärid" or u == "paber" and x == "kivi" or u == "käärid" and x == "paber":
        print("user võitis")
        break
    else:
        print("viik")
        break

