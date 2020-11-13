symbol = input("type down a character: ")
height = int(input("chose triangle's height: "))

for i in range(0, height):  # prints spaces until the correct position of the top
     print(' ', end = '')  # no newline on next print
print(symbol)  # top = height + 1
     
for i in range(1, height):  # middle part
    for j in range(height - i):  # prints the left spaces
        print(' ', end = '') 
    print(symbol, end = '')  # prints symbol on the correct place
    for j in range((i - 1) * 2 + 1):  # inside spaces
        print(' ', end = '') 
    print(symbol)  # second symbol

for i in range(0, height * 2 + 1):  # bottom
    print(symbol, end = '') 