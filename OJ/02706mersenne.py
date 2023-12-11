import textwrap, math
p = int(input())
print(math.ceil(p / math.log2(10)), *textwrap.wrap('{:0500}'.format(pow(2, p, 10 ** 500) - 1), 50), sep='\n')
