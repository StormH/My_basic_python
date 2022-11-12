choice = input("enter  (+, -, *, /)")
if choice == '0':
    print('wrong input')

if choice in ('+', '-', '*', '/'):
    x = input("enter number 1:")
    y = input("enter number 2:")

    z = isinstance(x,(int, float)):
    s = isinstance(y,(int, float)):

        if choice == '+':
            print("result:", (x+y))
        elif choice == '-':
            print("result:", (x-y))
        elif choice == '*':
            print("result:", (x*y))
        elif choice == '/':
            if y != 0:
                print("result:", (x/y))
        else:
            print("divided by zero!")
    else:
        print("Wrong input")