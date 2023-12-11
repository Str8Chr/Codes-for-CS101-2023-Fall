def find(array, k, l, r):
    num = l
    for i in range(l + 1, r):
        if array[i] <= array[l]:
            array[i], array[num + 1] = array[num + 1], array[i]
            num += 1
    array[l], array[num] = array[num], array[l]
    if num == k:
        return array[num]
    if num > k:
        return find(array, k, l, num)
    return find(array, k, num + 1, r)


n = int(input())
*dis, = map(lambda x: sum(eval(x)), input().split())
*price, = map(int, input().split())
*ratio, = map(lambda x: x[0]/x[1], zip(dis, price))
cnt = 0
mid_price = find(price.copy(), n // 2, 0, n)
mid_ratio = find(ratio.copy(), (n - 1) // 2, 0, n)
for i in range(n):
    cnt += price[i] < mid_price and ratio[i] > mid_ratio
print(cnt)
