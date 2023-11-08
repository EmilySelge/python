a = float(input("külg a:"))
b = float(input("külg b:"))
c = float(input("külg c:"))
if a+b>c or b+c>a or a+c>b:
    if a == b and b == c and c == a:
        print("kolmnurk on võrdkülgne")
    elif a == b or a == c or b == c:
        print("kolmnurk on võrdhaarne")
    else:
        print("kolmurk on erikülgne")
else:
    print("selliste külgedega kolmnurka ei eksisteeri")