n = int(input())
res = []
for a in range(3, n + 1):
    for b in range(2, a):
        for c in range(2, b + 1):
            for d in range(2, c + 1):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    res.append((a, d, c, b))
res.sort()
for i in res:
    print('Cube = {}, Triple = ({},{},{})'.format(i[0], i[1], i[2], i[3]))