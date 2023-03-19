import heapq
from collections import deque

def process_events(N, events):
    not_called = deque(range(1, N + 1))
    called_but_not_yet = []
    called_but_not_yet_set = set()
    result = []

    for event in events:
        if event[0] == 1:
            called = not_called.popleft()
            heapq.heappush(called_but_not_yet, called)
            called_but_not_yet_set.add(called)
        elif event[0] == 2:
            _, x = event
            if x in called_but_not_yet_set:
                called_but_not_yet_set.remove(x)
        elif event[0] == 3:
            while called_but_not_yet:
                called_again = heapq.heappop(called_but_not_yet)
                if called_again in called_but_not_yet_set:
                    called_but_not_yet_set.remove(called_again)
                    result.append(called_again)
                    break

    return result

N, Q = map(int, input().split())

events = []
for _ in range(Q):
    event_input = list(map(int, input().split()))
    events.append(tuple(event_input))

result = process_events(N, events)

for i in range(len(result)):
    print(result[i])
