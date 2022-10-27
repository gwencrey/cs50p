menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

print("Enter all items:")

total = 0

while True:
    try:
        item = input().title()
        
        cost = menu[item]
        total = total + cost
    except KeyError:
        print("Previous item not on the menu")
    except EOFError:
        print("\n")
        break

print(f"Your total is ${total:.2f}")