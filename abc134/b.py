def minimum_watchers(N, D):
    range_covered = 2 * D + 1
    num_watchers = (N + range_covered - 1) // range_covered
    return num_watchers

N,D = map(int, input().split())
print(minimum_watchers(N, D))