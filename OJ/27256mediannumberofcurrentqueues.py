from bisect import insort
array = []
chart = []
first = 0
for i in range(int(input())):
    op = input()
    if op == 'del':
        array.remove(chart[first])
        first += 1
    elif op == 'query':
        mid = (array[(len(array)) // 2] + array[(len(array) - 1) // 2]) / 2
        print(int(mid) if mid % 1 == 0 else mid)
    else:
        num = int(op.split()[1])
        chart.append(num)
        insort(array, num)
