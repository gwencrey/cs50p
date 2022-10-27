# -*- coding: utf-8 -*-
d = {
     "apple": 130,
     "avocado": 50,
     "banana": 110,
     "cantaloupe": 50,
     "grapefruit": 60,
     "grapes": 90,
     "honeydew": 50,
     "kiwifruit": 90
 }

food = input("Give me a fruit: ").lower()

if food in d:
    print(f"Calories: {d[food]}")
else:
    print("That's not on my list")