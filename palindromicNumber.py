a = int(input("Enter a palindromic number: "))
aux1 = a
aux2 = 0

while int(a) != 0:  # int(a) in order to be able to operate with int
    aux2 = aux2 * 10 + int(a) % 10
    a /= 10

if aux1 == aux2:
    print("It's palindromic")
else:
    print("It isn't palindromic, sorry")
