n, a, b = map(int, input().split())
*water, = map(int, input().split())
l, r = 0, n - 1
a_ori, b_ori = a, b
cnt = 0
while l < r:
    a -= water[l]
    b -= water[r]
    if a < 0:
        a = a_ori - water[l]
        cnt += 1
    if b < 0:
        b = b_ori - water[r]
        cnt += 1
    l += 1
    r -= 1
print(cnt + (l == r and max(a, b) < water[l]))
