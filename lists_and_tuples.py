text = input(" enter anything you want ")
txt = list(text)
txt_1 = tuple(text)
print(txt[2::3], "-this is list", "\n", txt_1[2::3], "-this is tuple")
# #########################################

l_1 = [1, 2.1, "f", "2", 3, "1", 18, "df"]

my_list = []

for i in l_1:
    if type(i) == float:
        my_list.append(i)
    elif type(i) == int and i % 2 == 0:
        my_list.append(i)
    elif type(i) == int and i % 2 != 0:
        my_list.append(i ** 2)
    elif type(i) == str and i.isdigit():
        my_list.append(int(i)*3)
    else:
        my_list.append(-1)
print(my_list)

my_list = [i if type(i) == float else i if type(i) == int and i % 2 == 0 else i ** 2
if type(i) == int and i % 2 != 0 else int(i)*3 if type(i) == str and i.isdigit() else -1 for i in (l_1)]
print(my_list)