x, y = map(int, input().split())
t = bin(int(bin(x)[2:][::-1], 2) ^ int(bin(y)[2:][::-1], 2))[2:][::-1]
for i in range(len(t)):
    if t[i] == '1':
        print(int(bin(x)[2:i + 2], 2))
        break
else:
    print(x)