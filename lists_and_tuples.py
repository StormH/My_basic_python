# text = input(" enter anything you want ")
# txt = list(text)
# txt_1 = tuple(text)
# print(txt[2::3], "-this is list", "\n", txt_1[2::3], "-this is tuple")
#########################################

m_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]

gen = []

for i in m_list:
    gen.append(i)
    
gen_ternary = [el if el.isdigit() else -1 for el in m_list]
print(f"{gen_ternary=}")