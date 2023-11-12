# Recognize the counterfeit coin among 12 coins using 3 weighings


n = int(input())
for i in range(n):
    # 1 for heavy, -1 for light, 0 for normal, 2 for unknown
    coins = {chr(65 + i): 2 for i in range(12)}
    for j in range(3):
        left, right, result = input().split()
        if result == 'even':
            for c in left + right:
                coins[c] = 0
        elif result == 'up':
            for c in left:
                if coins[c] == 2:
                    coins[c] = 1
                if coins[c] == -1:
                    coins[c] = 0
            for c in right:
                if coins[c] == 2:
                    coins[c] = -1
                if coins[c] == 1:
                    coins[c] = 0
            for c in coins:
                if c not in left + right:
                    coins[c] = 0
        else:
            for c in left:
                if coins[c] == 2:
                    coins[c] = -1
                if coins[c] == 1:
                    coins[c] = 0
            for c in right:
                if coins[c] == 2:
                    coins[c] = 1
                if coins[c] == -1:
                    coins[c] = 0
            for c in coins:
                if c not in left + right:
                    coins[c] = 0
    # print(coins)
    cntrft = [k for k, v in coins.items() if v][0]
    print(
        f'{cntrft} is the counterfeit coin and it is {"heavy" if coins[cntrft] == 1 else "light"}.')
