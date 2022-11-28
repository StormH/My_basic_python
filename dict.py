my_set = {i: chr(i) for i in range(0, 129)}

print(my_set)


words = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz1234567890"

crypto = input("")
key = int(input(""))
crypto = crypto.lower()
crypt = ""
for letter in crypto:
    psn = words.find(letter)
    n_psn = psn + key
    if letter in words:
        crypt = crypt + words[n_psn]
    else:
        crypt = crypt + letter
print(crypt)





