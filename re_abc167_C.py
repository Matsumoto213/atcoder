def solve():
    from itertools import product
    min_ =  1 << 60
    for bit in product((0,1),repeat = N):
        judge = [0] * M
        price = 0
        for i in range(M):
            if bit[i]:
                price += C[i]
                # iのアルゴリズムをjudgeのそれぞれに代入する
                for j in range(M):
                    judge[j] += algorithm[i][j]
        print(judge,price,bit)             
        over_x = 0
        for i in judge:
            if i >= X:
                over_x += 1
        if over_x >= M:
            min_ = min(min_,price)
    return min_
        
N,M,X = map(int, input().split())
C = []
algorithm = []
for i in range(N):
    c,*A = list(map(int, input().split()))
    C.append(c)
    algorithm.append(A)

ans = solve()
print(-1 if ans == 1 << 60 else ans)