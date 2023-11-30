from queue import Queue


def next_level():
    if expression.empty():
        return None
    s = expression.get()
    if s in '+-*/':
        return '(' + next_level() + s + next_level() + ')'
    return s


expression = Queue()
for i in input().split():
    expression.put(i)
print(f'{eval(next_level()):.6f}')
