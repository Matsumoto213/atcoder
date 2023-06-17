N = int(input())
A = list(map(int, input().split()))

def sort_based_on_f(A):
    indices = {}
    for i in range(len(A)):
        if A[i] not in indices:
            indices[A[i]] = [i]
        else:
            indices[A[i]].append(i)
    sorted_numbers = sorted([(i, indices[i][1]) for i in indices], key=lambda x: x[1])
    return [number for number, _ in sorted_numbers]

ans = sort_based_on_f(A)
print(*ans)