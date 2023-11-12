# a refined version of OJ\02692counterfeitcoin.py


def IsFake(coin):
    global results
    if all(
        (coin in results[j][0] and results[j][2] == 'down') or (
            coin in results[j][1] and results[j][2] == 'up') or (
            coin not in results[j][0] and coin not in results[j][1] and
            results[j][2] == 'even') for j in range(3)):
        return -1
    elif all(
        (coin in results[j][0] and results[j][2] == 'up') or (
            coin in results[j][1] and results[j][2] == 'down') or (
            coin not in results[j][0] and coin not in results[j][1] and
            results[j][2] == 'even') for j in range(3)):
        return 1
    else:
        return 0


n = int(input())
for i in range(n):
    results = []
    for j in range(3):
        results.append(list(input().split()))
    for coin in 'ABCDEFGHIJKL':
        if IsFake(coin):
            output = 'light' if IsFake(coin) == -1 else 'heavy'
            print(f'{coin} is the counterfeit coin and it is {output}.')
