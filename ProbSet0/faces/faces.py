# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:49:19 2022

@author: gwendolyn.reynolds
"""

def main():
    statement = input("Give me a face: ")
    
    faceStatement = convert(statement)
    
    print(faceStatement)

def convert(faceStr):
    faceStr = faceStr.replace(":)", "🙂")
    faceStr = faceStr.replace(":(", "🙁")
    
    return faceStr

main()
    