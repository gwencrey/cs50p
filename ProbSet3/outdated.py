# -*- coding: utf-8 -*-
print("Outdated")

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Give me a date: ").replace(",", "")
        
        if date.replace(" ", "").isalnum():
            parts = date.split()
            #Check parts
            if len(parts) != 3:
                raise ValueError
                
            #Check month
            if parts[0].isalpha():
                month_val = months.index(parts[0]) + 1
            
            #Check day
            if len(parts[1]) > 2 or parts[1].isnumeric() == False:
                raise ValueError
            else:
                day_val = int(parts[1])
                
            #Check year
            if len(parts[2]) != 4 or parts[2].isnumeric() == False:
                raise ValueError
            else:
                year_val = int(parts[2])
                
        elif date.replace("/", "").isnumeric():
            parts = date.split("/")
            
            #Check parts
            if len(parts) != 3:
                raise ValueError
            
            #Check month
            if len(parts[0]) > 2:
                raise ValueError
            else:
                month_val = int(parts[0])
                
                if month_val > 12 or month_val < 0:
                    raise ValueError
            
            #Check day
            if len(parts[1]) > 2:
                raise ValueError
            else:
                day_val = int(parts[1])
                
            #Check year
            if len(parts[2]) != 4:
                raise ValueError
            else:
                year_val = int(parts[2])
        else:
            raise ValueError
            
        break
    except ValueError:
        print("Date format not supported")
    except EOFError:
        print("\n")
        break

print(f"{year_val}-{month_val:02}-{day_val:02}")