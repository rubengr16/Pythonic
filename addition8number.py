add = 0
num = []  # empty array

for i in range(1,9):  # i from 1 to 9 iterates (8 total iterations)
    print("Enter value number", i, ": ")
    num.append(int(input()))  # fill list & cast

for i in range(8):
    add += num[i]

print("\n Al sumar los elementos de esta lista", num, "obtenemos", add)
