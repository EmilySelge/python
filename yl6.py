a = input("sisesta arv: a:")
b = input("sisesta arv: b:")
c = input("sisesta arv: c:")

if int(a)> int(b)> int(c):
    print(a ,"on suurem kui", b, c)
elif int(b) > int(c):
    print(b, "on suurem kui", c)
else:
    print(c, "on suurem kui", a, b)
