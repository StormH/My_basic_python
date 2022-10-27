comparison_result: bool = 3 != 5
print(comparison_result)

comparison_result: bool = 5 <= 5
print(comparison_result)

comparison_result: bool = 5 >= 5
print(comparison_result)

comparison_result: bool = 5 == 5
print(comparison_result)

is_true = True or True and False
print(is_true)

is_true = True and True or False
print(is_true)

is_true = True or True or False
print(is_true)

is_true = True or not True or False
print(is_true)

is_true = True and True or not False
print(is_true)

print(bool(None) == bool(7))

print(bool(" ") == bool(10 - 1))

print(bool('Hello') == bool(True or False))

print(type(bool(None)) == id(bool(None)))
