from queue import LifoQueue
s = LifoQueue()
for i in input():
    s.put(i)
    if s.queue[-1] == ']':
        s.get()
        part = str()
        while s.queue[-1] != '[':
            part += s.get()
        s.get()
        digit = str()
        while part[-1].isdigit():
            digit += part[-1]
            part = part[:-1]
        digit = int(digit)
        s.put(part * digit)
print(''.join(map(lambda x: x[::-1], s.queue)))
