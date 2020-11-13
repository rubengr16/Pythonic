symbol = input("type down a character: ")
height = int(input("chose triangle's height: "))

for i in range(0, height):
    for j in range(0, height - i):
        print(' ', end='')  # no newline, to separate args sep = ''
    for j in range(0, i*2 + 1):    
        print(symbol, end='')
    print("")  # newline
