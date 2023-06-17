import heapq

import heapq

import heapq

def solve(N, K, Q, queries):
    A = [0]*N
    h1, h2 = [], []  # h1 for storing the top K elements, h2 for others

    for X, Y in queries:
        X -= 1  # 0-indexed
        old_value = A[X]
        A[X] = Y
        if len(h1) < K or (h1 and h1[0][0] < A[X]):
            heapq.heappush(h1, (A[X], X))
            if len(h1) > K:
                _, idx = heapq.heappop(h1)
                if idx != X:
                    heapq.heappush(h2, (-A[idx], idx))
        else:
            heapq.heappush(h2, (-A[X], X))

        # remove outdated elements in h1
        while h1 and h1[0][0] != A[h1[0][1]]:
            _, idx = heapq.heappop(h1)
            if idx != X:
                heapq.heappush(h2, (-A[idx], idx))
        # remove outdated elements in h2
        while h2 and h2[0][0] != -A[h2[0][1]]:
            heapq.heappop(h2)

        print(sum(i[0] for i in h1) if len(h1) == K else sum(i[0] for i in h1) + old_value)


N,K,Q = map(int, input().split())
query = []

for i in range(Q):
    x,y = map(int, input().split())
    query.append((x,y))
solve(N, K, Q, query)