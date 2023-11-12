# 薛晋 2023.9.19
def get_inversion(string):
    inversion = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] > string[j]:
                inversion += 1
    return inversion


n, m = map(int, input().split())
lis = [input() for _ in range(m)]
lis.sort(key=lambda x: get_inversion(x))
for i in lis:
    print(i)
