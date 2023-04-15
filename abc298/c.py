N = int(input())
Q = int(input())

queries = []
for i in range(Q):
    q = list(map(int, input().split()))
    queries.append(q)


def process_queries(queries):
    boxes = [[] for _ in range(N)]
    cards = {}
    results = []

    for query in queries:
        if query[0] == 1:
            _, i, j = query
            boxes[j - 1].append(i)

            if i not in cards:
                cards[i] = set()
            cards[i].add(j)

        elif query[0] == 2:
            _, i = query
            box = sorted(boxes[i - 1])
            results.append(box)

        elif query[0] == 3:
            _, i = query
            if i in cards:
                results.append(sorted(cards[i]))
            else:
                results.append([])

    return results

def print_results(results):
    for result in results:
        print(" ".join(map(str, result)))

results = process_queries(queries)
print_results(results)