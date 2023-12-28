from itertools import count
while n := int(input()):
    def valid(length, dep=0):
        if dep == n and length == 0:
            return True
        if length == 0:
            length = ans
        for i in range(n):
            if used[i] or sticks[i] > length or (i and sticks[i] == sticks[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            if valid(length - sticks[i], dep + 1):
                return True
            used[i] = False
            if sticks[i] == length or length == ans:
                break
        return False

    *sticks, = map(int, input().split())
    sticks.sort(reverse=True)
    used = [False] * n
    lenSum = sum(sticks)
    for ans in count(sticks[0]):
        if lenSum % ans == 0:
            if valid(ans):
                print(ans)
                break

