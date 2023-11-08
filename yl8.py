year = int(input("sisesta aasta:"))
if year % 400 == 0 or (year % 4 == 0  and year % 100 != 0):
    print(year, "on liigaasta")
else:
    print(year, "on lihtaasta")