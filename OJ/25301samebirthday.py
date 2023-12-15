from collections import defaultdict
birthdays = defaultdict(list)
for _ in range(int(input())):
    ID, month, day = input().split()
    birthdays[(int(month), int(day))].append(ID)
for month, day in sorted(birthdays):
    if len(birthdays[(month, day)]) > 1:
        print(month, day, *birthdays[(month, day)])
