# 効率よく求めるために差分の計算だけ行わないようにしよう
N = int(input())
a = list(map(int, input().split()))
b = [0] + a + [0]
dis = 0
for i in range(len(b) - 1):
    dis += abs(b[i + 1] - b[i])

for j in range(len(a)):
    if j == 0:
        x = 0
    else:
        x = a[j - 1]
    
    
    if j == N - 1:
        z = 0
    else:
        z = a[j + 1]
    
    y = a[j]
    ans = dis
    
    ans -= abs(x - y)
    ans -= abs(y - z)
    ans += abs(x - z)
    
    print(ans)
    