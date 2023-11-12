input()
l = list(map(int, input().split()))
l.sort()
sums = 0
cnt = 0
for i in l:
    if i >= sums:
        cnt += 1
        sums += i
print(cnt)