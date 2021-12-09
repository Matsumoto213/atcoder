# 計算量の問題でアウト
N,K = map(int, input().split())
dic = {}
A = []
for i in range(N):
    a,b = map(int, input().split())
    if a in A:
        dic[a] += b
    else:
        dic[a] = b
    A.append(a)
        
village = 0
while K:
    K -= 1
    village += 1
    
    if village in A:
        K += dic[village]
print(village)