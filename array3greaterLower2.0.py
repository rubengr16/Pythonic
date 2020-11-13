# arranging 3 elements vector without aux
num = []
while len(num) != 3 or num[0] == num[1] or num[1] == num[2]:  # fill no repetitions
    for i in range(3):
        num.append(int(input("enter value:")))
while num[1] > num[0] or num[2] > num[1]:   # repeat until values are on their position
    if num[2] > num[1]:  # 2 greater than 1
        num[1] += num[2]
        num[2] = num[1] - num[2]
        num[1] -= num[2]
    if num[1] > num[0]:  # 1 greater than 0
        num[0] += num[1]
        num[1] = num[0] - num[1]
        num[0] -= num[1]

print(num[0], "is the greatest and", num[2], "the lower")
