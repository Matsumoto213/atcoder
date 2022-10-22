N,A,B = map(int, input().split())
ans = []

for i in range(1,N + 1):
    i = str(i)
    temp = [int(i[j]) for j in range(len(i))]
    sumDigit = sum(temp)
    if sumDigit >= A and sumDigit <= B:
        ans.append(int(i))
print(sum(ans))