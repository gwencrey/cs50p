# -*- coding: utf-8 -*-
statement = input("Tweet something: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

i = 0
state_len = len(statement)
new_statement = ""
for i in range(state_len):
    if statement[i] not in vowels:
        new_statement = new_statement + statement[i]

print(new_statement)
        