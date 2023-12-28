from itertools import permutations
print(*map(lambda x: ''.join(x), permutations(sorted(input()))), sep='\n')