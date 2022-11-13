txt = input("enter the words")

for upper in txt:
    if upper.isupper():
        print(upper)
    continue

for index, element in enumerate(txt):
    if element.isspace():
        print(f"{index=}|{element}")
    continue

for las in txt:
    if las in "aeiouAEIOU":
        print(las)

digit = input("something")
digits = ''
for num in digit:
    if num.isdigit():
        digits += num

        if len(digits) == 3:
            break
    print(num)
else:
    print("all ok")
##########################################
# while True:
#     choice = input("enter  (+, -, *, /)")
#     if choice == '0':
#         print('wrong input')
#     if choice == "exit":
#         break
#     if choice in ('+', '-', '*', '/'):
#         x = input("enter number 1:")
#
#         try:
#             x = int(x)
#         except:
#             x = float(x)
#         y = input("enter number 2:")
#
#         try:
#             y = int(y)
#         except:
#             y = float(y)
#
#         if choice == '+':
#             print("result:", (x + y), type(x+y))
#         elif choice == '-':
#             print("result:", (x - y), type(x-y))
#         elif choice == '*':
#             print("result:", (x * y), type(x*y))
#         elif choice == '/':
#             if y != 0:
#                 print("result:", (x / y), type(x / y))
#             else:
#                 print("divided by zero!")
#     else:
#         print("Wrong input")
