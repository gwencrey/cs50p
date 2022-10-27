#try:
#    x = int(input("Give me x: "))
#except ValueError:
#    print("x is not an integer")
#else:
#    print(f"x is {x}")

def main():
    x = get_int()
    print(f"x is {x}")
    
    x = get_int2("Give me x: ")
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            x = int(input("Give me x: "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

def get_int2(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
