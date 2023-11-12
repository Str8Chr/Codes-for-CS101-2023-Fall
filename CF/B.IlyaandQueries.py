s = input()
query = [0] * len(s)
for i in range(1, len(s)):
    query[i] = query[i - 1] + (s[i] == s[i - 1])
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(query[r - 1] - query[l - 1])
