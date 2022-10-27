# -*- coding: utf-8 -*-
def main():
    var_name = input("Give me a variable name: ")
    
    var_name_new = get_camel(var_name)
    
    print(var_name_new)

def get_camel(str_val):
    letter = 1
    while str_val.islower() == False and letter < len(str_val):
        tf = str_val[letter].isupper()
        
        if tf == True:
            str_val = str_val[0:letter] + "_" + str_val[letter].lower() + str_val[letter+1:]
        
        letter += 1
    
    return str_val
    
main()