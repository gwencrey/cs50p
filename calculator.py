# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:28:42 2022

@author: gwendolyn.reynolds
"""

def main():
    x = int(input("x: "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()