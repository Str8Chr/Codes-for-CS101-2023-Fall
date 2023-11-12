s = input()
hello = ['h', 'e', 'l', 'l', 'o']
i = 0
for c in s:
    if c == hello[i]:
        i += 1
    if i == 5:
        break
if i == 5:
    print("YES")
else:
    print("NO")