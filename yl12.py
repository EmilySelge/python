fruitlist = ["õun", "pirn", "banaan"]
print (fruitlist[0])

fruitlist.append("ploom")
print (fruitlist[3])

fruitlist[2] = "kirss"
print (fruitlist)

if "õun" in fruitlist:
    print ("õun on listis")

print (len(fruitlist))

fruitlist.pop(1)
print(fruitlist)

fruitlist.reverse()

fruitlist.sort()
print (fruitlist)