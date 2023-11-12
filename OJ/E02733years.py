y = int(input())
if y % 100 != 0 and y % 4 == 0 or y % 400 == 0 and y % 3200 != 0:
    print('Y')
else:
    print('N')