from re import U


N = int(input())
# これで習得済みかを判断する
judge = [False] * N

# i単体で何時間かかるかを記載
num = [0] * N
L = []

for i in range(N):
    l = list(map(int, input().split()))
    num[i] = l[0]
    L.append(l)

