#to calculate the minimum number of cards needed
#to achieve an overhang of at least c card lengths

lists = []
c = float(input())
while c:
    lists.append(c)
    c = float(input())

count = 0
for i in lists:
    count += 1
    summ = 0
    n = 0
    while summ < i:
        n += 1
        summ += 1/(n+1)
    if count != len(lists):
        print(n, "card(s)")
    else:
        print(n, "card(s)", end = "")