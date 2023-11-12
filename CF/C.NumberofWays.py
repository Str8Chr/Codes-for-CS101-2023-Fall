from bisect import bisect_right as br
n = int(input())
*array, = map(int, input().split())
s = sum(array)
l, r = 0, n - 1
ansL = []
ansR = []
ans = sumL = sumR = 0
while l < n:
    sumL += array[l]
    sumR += array[r]
    if sumL == s / 3: ansL.append(l)
    if sumR == s / 3: ansR.append(r)
    l += 1; r -= 1
for i in ansR:
    ans += br(ansL, i - 2)
print(ans)