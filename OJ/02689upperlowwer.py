st = input()
lis = list(st)
for i in range(len(lis)):
    if 97 <= ord(lis[i]) <= 122:
        lis[i] = chr(ord(lis[i]) - 32)
    elif 65 <= ord(lis[i]) <= 90:
        lis[i] = chr(ord(lis[i]) + 32)
print(''.join(lis))
