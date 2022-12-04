my_set = set(input())
my_set_2 = set(input())

print(my_set.intersection(my_set_2))
print(my_set.difference(my_set_2))

my_set |= my_set_2  # Обновить набор, добавив элементы из всех остальных
my_set -= my_set_2  # Обновить набор, удалив элементы, найденные в других
my_set &= my_set_2  # Обновить набор, сохранив только найденные в нем элементы и все остальные.
my_set ^= my_set_2  # Обновить набор, сохранив только элементы, найденные в любом наборе, но не в обоих.

print(my_set)
print(my_set,my_set_2)