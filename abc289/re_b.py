N,M = map(int, input().split())
A = list(map(int, input().split()))
ans = []
numbers = []
for i in range(1, N + 1):
    if i in A:
        numbers.append(i)
    else:
        ans.append(i)
        numbers.reverse()
        ans.extend(numbers)
        numbers = []
print(*ans)