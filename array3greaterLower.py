num = []
aux = 0
while len(num) != 3 or num[0] == num[1] or num[1] == num[2]:  # 3 different values
    for i in range(3):
        num.append(int(input("enter value:")))

while num[1] > num[0] or num[2] > num[1]:  # until values are arranged correctly
    if num[2] > num[1]:  # arrangement of 2 and 1
        aux = num[2]
        num[2] = num[1]
        num[1] = aux
    if num[1] > num[0]:  # 1 and 0
        aux = num[0]
        num[0] = num[1]
        num[1] = aux

print(num[0], "is the greater number and", num[2], "the lower")
