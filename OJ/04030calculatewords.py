i, pattern, toMatch = 0, input().lower().strip(), input().lower()
while pattern in toMatch:
    if (toMatch.find(pattern) + len(pattern) >= len(toMatch) or
            (toMatch[toMatch.find(pattern) + len(pattern)] == ' ' and
             (toMatch.find(pattern) == 0 or toMatch[toMatch.find(pattern) - 1] == ' '))):
        i += toMatch.find(pattern)
        toMatch = toMatch[toMatch.find(pattern):].split()
        print(toMatch.count(pattern), i)
        break
    else:
        j = 0
        for j in range(toMatch.find(pattern) + len(pattern), len(toMatch)):
            if toMatch[j] == ' ':
                break
        i += j
        toMatch = toMatch[j:]
else:
    print(-1)
