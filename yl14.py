file = input("sisesta faili nimi:")
x = file.split(".")
if ".ext" in file:
    print(x[1])

else:
    print("faili nimi pole kujul '.ext'")