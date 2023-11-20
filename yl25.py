dictionary = {
    "eesnimi": "Emily",
    "perenimi": "Selge",
    "sünniaasta": 2007,
    "elukoht": "Kuressaare",
    "magustoit": "jäätis"
}

e = dictionary.get("elukoht")
print(e)


print(dictionary["elukoht"])


dictionary["magustoit"] = "pannkook"
print(dictionary["magustoit"])


for x in dictionary:
    print(x)


for y in dictionary.values():
    print(y)


for i in dictionary:
    print(dictionary[i])


if "isikukood" in dictionary:
    print("isikukood on olemas")
else:
    print("isikukoodi ei ole")


print(len(dictionary))

dictionary["pikkus"] = "168cm"
print(dictionary["pikkus"])

dictionary.pop("sünniaasta")

del dictionary["sünniaasta"]

del dictionary

dictionary.clear()