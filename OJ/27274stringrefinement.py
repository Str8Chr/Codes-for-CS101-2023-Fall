s, m, res = input(), 0, []
while 2 ** m <= len(s): res.append(s[2 ** m - 1]); m += 1
print(''.join([[res[:(len(res) + 1) // 2], res[len(res) - 1:(len(res) + 1) // 2 - 1:-1]][i % 2][i // 2] for i in range(len(res))]))
