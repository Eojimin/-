N = input()
mini = 0
alphabet = []
number = []
result = ""
for i in N:
    if ord(i) < 65:
        number.append(int(i))
    else:
        alphabet.append(ord(i))
alphabet.sort()
for n in alphabet:
    result += chr(n)
result += str(sum(number))
print(result)



