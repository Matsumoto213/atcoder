n,k,m = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)
for i in range(k + 1):
    ans = total + i
    average = ans // n
    if average >= m:
        print(i)
        exit()
print(-1)