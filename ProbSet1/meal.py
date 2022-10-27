# -*- coding: utf-8 -*-

def main():
    now = input("What time is it? ")
    
    now = convert(now)
    
    if 7 <= now <= 8:
        print("breakfast time")
    elif 12 <= now <= 13:
        print("lunch time")
    elif 18 <= now <= 19:
        print("dinner time")


def convert(time):
    hrs, mins = time.split(":")
    
    hrs = int(hrs) + (int(mins)/60)
    
    return hrs


if __name__ == "__main__":
    main()