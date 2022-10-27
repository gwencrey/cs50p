# -*- coding: utf-8 -*-

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("n: "))
        if n > 0:
            return n
    
def meow(n):
    for __ in range(n):
        print("meow")

main()