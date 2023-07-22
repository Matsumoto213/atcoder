N,D = map(int, input().split())
S = [input() for _ in range(N)]

def max_free_days(N, D, schedules):
    free_days = [True] * D

    for i in range(N):
        for j in range(D):
            if schedules[i][j] == 'x':
                free_days[j] = False

    max_count = count = 0
    for day in free_days:
        if day:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

print(max_free_days(N, D, S))