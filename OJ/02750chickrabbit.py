n = int(input())
if n % 2 == 0:
    minimum = n // 4 + n % 4 // 2
    maximum = n // 2
    print(minimum, maximum)
else:
    print('0 0')
