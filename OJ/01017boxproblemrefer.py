rest_for_b = [0, 5, 3, 1]
while True:
    a, b, c, d, e, f = map(int, input().split())
    if a == b == c == d == e == f == 0:
        break
    ans = f + e + d + (c + 3) // 4  # 3 * 3至6 * 6的箱子
    sapce_for_b = 5 * d + rest_for_b[c % 4]  # 2 * 2的箱子可用空间
    if b > sapce_for_b:
        ans += (b - sapce_for_b + 8) // 9
    sapce_for_a = 36 * ans - 36 * f - 25 * e - 16 * d - 9 * c - 4 * b
    if a > sapce_for_a:
        ans += (a - sapce_for_a + 35) // 36
    print(ans)