from collections import defaultdict
N,Q = map(int,input().split())
a = list(map(int,input().split()))

# defaultdictでそれぞれの値のインデックスが生成される
A_dic=defaultdict(list)
for i in range(N):
    A_dic[a[i]].append(i+1)

for i in range(Q):
    x,k = map(int,input().split())
    if len(A_dic[x]) >= k:
        print(A_dic[x][k - 1])
    else:
        print(-1)