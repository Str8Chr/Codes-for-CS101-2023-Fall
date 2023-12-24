s = input().lower(); orig, new = map(lambda x: x.lower(), input().split()); i = 0
while i < len(s):
    if s[i:].startswith(orig) and (i + len(orig) == len(s) or not s[i + len(orig)].isalpha()):
        s = s[:i] + new + s[i + len(orig):]
        i += len(new)
    else: i += 1
for i in range(len(s)):
    if s[i].isalpha() and i == 0 or i > 1 and s[i - 2] == '.' and s[i - 1] == ' ' or\
            i > 0 and s[i - 1] == ' ' and s[i - 1] == '.': s = s[:i] + s[i].upper() + s[i + 1:]
print(s)
