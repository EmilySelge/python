

def upc(number):
    n = str(number)
    odd = sum([int(n[i]) for i in range(11) if i % 2 == 0])
    x = odd * 3
    even = sum([int(n[i]) for i in range(11) if i % 2 != 0])
    y = x + even
    m = y % 10
    if m == 0:
        print(0)
    else:
       l = 10 - m
       print(l)

upc("09876543212")

