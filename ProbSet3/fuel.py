# -*- coding: utf-8 -*-

while True:
    try:
        frac = input("What does the fuel guage say? ")
    
        nums = frac.split("/")
        
        if len(nums) != 2:
            raise ValueError
            
        numerator = int(nums[0])
        denominator = int(nums[1])
        
        percent = int(round((numerator/denominator)*100, 0))
        
        if percent < 0 or percent > 100:
            raise ValueError
        
        break
    except ValueError:
        print("Numerator/denominator format not accepted")
    except ZeroDivisionError:
        print("Cannot divide by zero")

if percent < 1:
    print("E")
elif percent > 99:
    print("F")
else:
    print(f"{percent}%")