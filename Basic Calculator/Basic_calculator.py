# The functions we have created : add, sub, mul, div, mod, power
# prints option to user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a,b):
    answer = a + b
    print( a , "+", b , "=" , answer , '\n')

def sub(a,b):
    answer = a - b
    print( a , "-" , b , "=" , answer , '\n')
    

def mul(a,b):
    answer = a * b
    print( a , "*" , b , "=" , answer , '\n')

def div(a,b):
    answer = a / b
    print( a , "/" , b , "=" , answer , '\n')

def mod(a,b):
    answer = a % b
    print( a , "%" , b , "=" , answer , '\n')

def power(a,b):
    answer = a ** b
    print( a , "**" , b , "=" , answer , '\n')

while True:

    print("Welcome to my calculator")
    print('A for Addition')
    print('S for Subtraction')
    print('M for Mutiplication')
    print('D for Division')
    print('M for Modulo')
    print('P for Power')
    print('E for Exit')

    choice = input('Enter what you like to do: ')

    if choice == 'a' or choice == 'A':
        print('You chose Addition')
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a,b)

    elif choice == 's' or choice == 'S':
        print('You chose Subtraction')
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a,b)

    elif choice == 'm' or choice == 'M':
        print('You chose Multiplication')
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a,b)

    elif choice == 'd' or choice == 'D':
        print('You chose Division')
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a,b)

    elif choice == 'x' or choice == 'X':
        print('You chose Modulo')
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mod(a,b)

    elif choice == 'p' or choice == 'P':
        print('You chose Power')
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        power(a,b)

    elif choice == 'e' or choice == 'E':
        print('Thank you ')
        quit()













    








