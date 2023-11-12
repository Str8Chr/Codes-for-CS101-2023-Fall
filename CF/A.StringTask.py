vowels = ['a', 'o', 'y', 'e', 'u', 'i']
s = input()
s = list(s.lower())
for i in range(len(s)):
    if s[i] in vowels:
        s[i] = ''
    else:
        s[i] = '.' + s[i]
print(''.join(s))