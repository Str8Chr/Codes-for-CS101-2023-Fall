fibonacci = []


def gen(n):
    for i in range(n + 1):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])


x = [int(input()) for _ in range(int(input()))]
gen(max(x))
for j in x:
    print(fibonacci[j])

