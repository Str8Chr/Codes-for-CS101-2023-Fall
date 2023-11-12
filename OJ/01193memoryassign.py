from queue import PriorityQueue, Queue


class Seg(object):
    next = None
    prev = None
    ans = 0

    def __init__(self, l, r, go):
        self.left = l
        self.right = r
        self.go = go

    def __lt__(self, other):
        return self.go < other.go

    def leave(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        Seg.ans = self.go + 1


class Process(object):
    def __init__(self, t, m, p):
        self.t = t
        self.m = m
        self.p = p

    def enter(self, q):
        x = start
        while x != end:
            if x.next.left - x.right - 1 >= self.m:
                now = Seg(x.right + 1, x.right + self.m, self.t + self.p - 1)
                now.next = x.next
                now.prev = x
                x.next.prev = now
                x.next = now
                q.put(now)
                return True
            x = x.next
        return False


q = PriorityQueue()
waiting = Queue()
processes = []
waiting_cnt = 0
n = int(input())
start = Seg(0, 0, 0)
end = Seg(n + 1, n + 1, 0)
start.next = end
end.prev = start
while True:
    t, m, p = map(int, input().split())
    if t == m == p == 0: break
    processes.append(Process(t, m, p))
for process in processes:
    while not q.empty():
        if q.queue[0].go < process.t:
            top = q.get()
            t = top.go + 1
            top.leave()
            if not q.empty() and q.queue[0].go + 1 == t: continue
            while (not waiting.empty() and
                   Process(t, waiting.queue[0].m, waiting.queue[0].p).enter(q)):
                waiting.get()
        else: break
    if not process.enter(q):
        waiting.put(process)
        waiting_cnt += 1
while not q.empty():
    top = q.get()
    t = top.go + 1
    top.leave()
    if not q.empty() and q.queue[0].go + 1 == t: continue
    while (not waiting.empty() and
           Process(t, waiting.queue[0].m, waiting.queue[0].p).enter(q)):
        waiting.get()
print(Seg.ans, waiting_cnt, sep='\n')
