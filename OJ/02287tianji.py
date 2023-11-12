while n := int(input()):
    Tianji = sorted(list(map(int, input().split())))
    Qiwang = sorted(list(map(int, input().split())))
    t0 = q0 = 0
    t1 = q1 = n - 1
    cnt = 0
    while t0 <= t1:
        if Tianji[t0] > Qiwang[q0]:
            cnt += 1
            t0 += 1
            q0 += 1
        elif Tianji[t1] > Qiwang[q1]:
            cnt += 1
            t1 -= 1
            q1 -= 1
        elif Tianji[t0] < Qiwang[q1]:
            cnt -= 1
            t0 += 1
            q1 -= 1
        else:
            t0 += 1
            q1 -= 1
    print(cnt * 200)