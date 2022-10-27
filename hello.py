def main():
    # Ask user for name
    name = input("Name: ")
    
    hello(name)
    
def hello(to="world"):
    print("hello,", to)
    
main()