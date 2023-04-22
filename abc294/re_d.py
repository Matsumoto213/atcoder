N,Q = map(int, input().split())
events = [tuple(map(int, input().split())) for _ in range(Q)]

import heapq

from collections import deque

def bank_events(n, events):
    called = [0 for _ in range(n + 1)]
    now = 0
    result = []

    for event in events:
        if event[0] == 1:
            while now < n and called[now] != 0:
                now += 1
            if now < n:
                called[now] = 1
        elif event[0] == 2:
            x = event[1]
            called[x - 1] = 1
        elif event[0] == 3:
            while now < n and called[now] != 0:
                now += 1
            if now < n:
                print(now + 1)
                called[now] = 1

    return result

result = bank_events(N, events)

for i in result:
    print(i)