from collections import deque

def topological_sort(graph, indegree):
    order = []
    q = deque()

    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        order.append(node)

        for adj in graph[node]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                q.append(adj)

    return order

def main():
    N = int(input())

    graph = [[] for _ in range(N)]
    indegree = [0] * N

    for i in range(N):
        C,*prerequisites = map(int, input().split())
        indegree[i] += C
        for p in prerequisites:
            graph[p-1].append(i)

    order = topological_sort(graph, indegree)
    books_to_read_before_1 = []

    # Track read books
    read = [False] * N
    for book in order:
        if book == 0:
            break
        books_to_read_before_1.append(book)
        read[book] = True

        # Mark prerequisites as read
        for prerequisite in graph[book]:
            if not read[prerequisite]:
                read[prerequisite] = True
                books_to_read_before_1.append(prerequisite)

    # Output
    for book in reversed(books_to_read_before_1):
        print(book + 1)

if __name__ == "__main__":
    main()