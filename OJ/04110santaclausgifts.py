N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append([v, w, v / w])
items.sort(key=lambda x: x[2], reverse=True)
ans = 0
for i in range(N):
    if W >= items[i][1]:
        ans += items[i][0]
        W -= items[i][1]
    else:
        ans += W * items[i][2]
        break
print('%.1f' % ans)