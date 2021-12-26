# 組み合わせを見ていくときに計算量を減らす方法
# forループを回すことなく全ての値を見ていくにはどうすればいいのか？
# こういうときに深さ優先探索を使うらしい

# 初めに一つ受け取っておいて後で受け取る値を元にforループを回す
N,X = map(int, input().split())
m,*T = map(int, input().split())

for i in range(N - 1):
    temp = []
    n,*b = list(map(int, input().split()))
    m = m * n
    
    for t in T:
        for j in b:
            temp.append(t*j)
            
    T = temp
print(T.count(X))
    
            


