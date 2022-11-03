number = float(input("enter the number"))
number_2 = float(input(" enter the second number"))

print('{} + {} = '.format(number, number_2))
print(number + number_2)

print('{} - {} = '.format(number, number_2))
print(number - number_2)

print('{} * {} = '.format(number, number_2))
print(number * number_2)

print('{} ** {} = '.format(number, number_2))
print(number ** number_2)

print('{} / {} = '.format(number, number_2))

if number_2 == 0:
    print('cannot divide by zero')
else:
    print(number / number_2)

print(type(number))
print(type(number_2))

print(number == number_2)
print(number != number_2)

a = number or number_2
if a < 100:
    print('Low')
elif 0 <= a <= 100:
    print('Mid')
else:
    print('High')

