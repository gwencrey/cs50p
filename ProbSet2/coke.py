# -*- coding: utf-8 -*-
total = 0
cost = 50

while total <= cost:
    print("Amount Due:", cost - total)    
    amount = input("Insert Coin: ")
    
    amount = int(amount) 
    
    if amount == 25 or amount == 10 or amount == 5:
        total = total + amount

change = total - cost

print("Here's a coke! Change due:", change)