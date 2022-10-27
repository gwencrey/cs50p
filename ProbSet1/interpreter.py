# -*- coding: utf-8 -*-

x, y, z = input("Give me an expression: ").split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(float(x/z))
else:
    print("I'm confused")
    
