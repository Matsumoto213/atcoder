Q = int(input())

queries = []
for i in range(Q):
    q = list(map(int, input().split()))
    queries.append(q)

def process_queries(queries):
    S = ['1']
    pow_ten = [1]
    MOD = 998244353
    results = []

    for query in queries:
        if query[0] == 1:
            _, x = query
            S.append(str(x))
            pow_ten.append((pow_ten[-1] * 10) % MOD)

        elif query[0] == 2:
            if S:
                S.pop(0)
                pow_ten.pop(0)

        elif query[0] == 3:
            result = sum(int(s) * p for s, p in zip(S, pow_ten[::-1])) % MOD
            results.append(result)

    return results

results = process_queries(queries)

for i in range(len(results)):
    print(results[i])