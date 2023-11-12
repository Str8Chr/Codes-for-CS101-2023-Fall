x = 0
for _ in range(int(input())):
    s = input()
    x += (s.count('+') - s.count('-')) / 2
print(int(x))
