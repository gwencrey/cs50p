# -*- coding: utf-8 -*-
g = {}

print("Give me groceries: \n")

while True:
    try:
        item = input().upper()
        
        if item in g:
            g[item] += 1
        else:
            g[item] = 1
    except EOFError:
        print("\n")
        break

for item in sorted(g.keys()):
    print(g[item], item, sep=" ")