# -*- coding: utf-8 -*-
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Check length
    if len(s) < 2 or len(s) > 6:
        return False
    
    #Check for special chars
    if s.isalnum() == False:
        return False
    
    #Check first 2 chars
    if s[0:2].isalpha() == False:
        return False
    
    #Check for numbers
    if s.isalpha() == False:
        #Find first letter
        for i in range(len(s)):
            if s[i].isdigit():
                #Check if its a zero
                if s[i] == "0":
                    return False
                
                if i < len(s):
                    #Check for letters after
                    if s[i+1:].isdigit() == False:
                        return False
                    else:
                        return True
    
    return True


main()
