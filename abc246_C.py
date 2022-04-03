N,K,X = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse = True)
i = 0
ans = 0
while True:
    if i == 0:
        A[i] -= X
        ans += 1
        temp = A[0]
    else:
        if temp > A[i]:
            i = 0
        else:
            ans += 1
            A[i] -= X
            A[i] = max(0,A[i])

        cnt = A.count(0)
        if ans == K or cnt == N:
            print(A)
            break
    print(A[i],i)
    i += 1


print(sum(A))