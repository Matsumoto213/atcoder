N,A,B = map(int,input().split())
ans = []

for i in range(1,N + 1):
    x = [int(a) for a in str(i)]
    temp = sum(x)

    if temp >= A and temp <= B:
        ans.append(i)
print(sum(ans))