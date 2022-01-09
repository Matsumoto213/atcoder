from collections import Counter
N = int(input())
D = list(map(int,input().split()))
# 予選問題にはM問が必要
M = int(input())
T = list(map(int,input().split()))

cnt_d = Counter(D)
cnt_t = Counter(T)


judge = True
for key,value in cnt_t.items():
    if cnt_d[key] < value:
        judge = False
    else:
        cnt_d[key] = cnt_d[key] - value
print('YES' if judge else 'NO')