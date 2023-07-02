N = int(input())
A = list(map(int, input().split()))

def calculate_weekly_steps(N, steps):
    weekly_steps = []
    for i in range(N):
        weekly_steps.append(sum(steps[i*7:(i+1)*7]))
    return weekly_steps
print(*calculate_weekly_steps(N, A))