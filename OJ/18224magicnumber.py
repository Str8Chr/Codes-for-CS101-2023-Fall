m = int(input())
*nums, = map(int, input().split())
for i in nums:
    for j in range(1, int(i ** 0.5) + 1):
        k = (i - j ** 2) ** 0.5
        if int(k) == k and k:
            print(bin(i), oct(i), hex(i))
            break
