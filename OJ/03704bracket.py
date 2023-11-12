from queue import LifoQueue


def main():
    s: str = input()
    matched = [0] * len(s)
    stack = LifoQueue()
    for c in range(len(s)):
        if s[c] == '(':
            stack.put(c)
        elif s[c] == ')':
            if stack.empty():
                matched[c] = 1
            else:
                stack.get()
    while not stack.empty():
        matched[stack.get()] = -1
    print(s)
    print(''.join([' ' if x == 0 else '?' if x == 1 else '$' for x in matched]))
    return 0


while True:
    try:
        main()
    except EOFError:
        break
