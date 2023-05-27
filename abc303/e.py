N = int(input())
edge = []

for i in range(N - 1):
    u,v = map(int, input().split())
    edge.append((u,v))

def star_graphs(edges):
    # Initialize graph as adjacency list
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a list to store degrees of vertices
    degrees = [0] * (len(graph) + 1)

    # Compute degrees of vertices
    for vertex in graph:
        degrees[vertex] = len(graph[vertex])

    # Initialize a variable to store the number of stars
    stars = 0
    # Initialize a list to store the levels of stars
    levels = []

    # For each vertex in the graph
    for vertex in graph:
        # If the degree of the vertex is greater than or equal to 2
        if degrees[vertex] >= 2:
            # Increment the number of stars
            stars += 1
            # Append the degree of the vertex to the levels of stars
            levels.append(degrees[vertex])

    # Return the number of stars and the levels of stars
    return stars, levels
print(star_graphs(edge))