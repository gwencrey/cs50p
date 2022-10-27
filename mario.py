# -*- coding: utf-8 -*-

def main():
    print_square(3)
    
    height = int(input("Height: "))
    pyramid(height)



def print_column(height):
    print("#\n" * height, end="")
          
def print_row(width):
    print("#" * width)

def print_square_long(dim):
    # For each row in square
    for i in range(dim):
        
        # For each brick in row
        for j in range(dim):
            
            #Print brick
            print("#", end="")
        
        # New line
        print()
        
def print_square(dim):
    # For each row in square
    for i in range(dim):
        print_row(dim)
        
def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))


if __name__ == "__main__":
    main()