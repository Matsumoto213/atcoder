N = int(input())
S = list(map(int, input().split()))

dict = {}
for i in range(N):
    dict[S[i]] = False

cnt = 0
for a in range(1,1001):
    for b in range(1,1001):
        temp = (4 * a * b) + (3 * a) + (3 * b)
        if temp in S:
            if dict[temp] == False:
                cnt += S.count(temp)
                dict[temp] = True     
print(len(S) - cnt)