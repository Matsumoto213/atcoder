Q = int(input())

queries = []
for i in range(Q):
    q = list(map(int, input().split()))
    queries.append(q)

from collections import deque

def process_queries(queries):
    S = deque([1])
    MOD = 998244353
    remainder = 1

    for query in queries:
        op = query[0]

        if op == 1:
            x = query[1]
            remainder = (remainder * 10 + x) % MOD
            S.append(x)
        elif op == 2:
            removed_digit = S.popleft()
            remainder = (remainder - removed_digit * pow(10, len(S), MOD)) % MOD
        elif op == 3:
            print(remainder)

process_queries(queries)