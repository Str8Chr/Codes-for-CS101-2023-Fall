max_sum = 0
for a1 in range(n := int(input()) + 1):
    for a2 in range(n):
        for a3 in range(n):
            if (a1 + a2) % 2 == 0 and (a2 + a3) % 3 == 0 and (a1 + a2 + a3) % 5 == 0:
                max_sum = max(max_sum, a1 + a2 + a3)
print(max_sum)