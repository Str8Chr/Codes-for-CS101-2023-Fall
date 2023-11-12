ans = []
for _ in range(int(input())):
    n = int(input())
    *times, = zip(map(int, input().split()), map(int, input().split()))
    times.sort(reverse=True)
    totalDlvTime = [times[i][0] for i in range(n)] + [0]
    totalPckTime = [0]
    for i in range(n):
        totalPckTime.append(totalPckTime[-1] + times[i][1])
    ans.append(min(map(max, totalDlvTime, totalPckTime)))
print(*ans, sep='\n')
