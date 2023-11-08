user = input("sisesta string:")
length = len(user)
middle = int((length - 1) // 2)
if (length >= 7) and not (length % 2) == 0:
    print(user.strip())
    print(user [middle - 1])
    print(user [middle])
    print(user [middle + 1])
else:
    print("sümboleid peab olema 7 või rohkem ja paaritus arvus")