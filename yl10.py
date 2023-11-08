name = input("nimi:")
print ("Tere!", name)
place = input("elukoht:")
if place == "Saaremaa" in place.lower():
    print ("Tere, Saarlane!")
age = int(input("vanus:"))
if age < 18:
    print ("Oled liiga noor, et autot juhtida")
elif age == 18:
    print ("Õnnitlused täisealiseks saamise puhul")
else:
    print ("võid autot juhtida")