choice = input("enter  (+, -, *, /)")
if choice == '0':
    print('wrong input')

if choice in ('+', '-', '*', '/'):
    x = input("enter number 1:")
    print(f"How many orders does the operand have?:", len(x))

    try:
        x = int(x)
    except:
        x = float(x)

    y = input("enter number 2:")
    print(f"How many orders does the operand have?:", len(y))

    try:
        y = int(y)
    except:
        y = float(y)

    if choice == '+':
        print("result:", (x+y), type(x+y))
    elif choice == '-':
        print("result:", (x-y), type(x-y))
    elif choice == '*':
        print("result:", (x*y), type(x*y))
    elif choice == '/':
        if y != 0:
            print("result:", (x/y),type(x/y))
        else:
            print("divided by zero!")
    else:
        print("Wrong input")