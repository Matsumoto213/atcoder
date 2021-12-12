N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
mi = 10 ** 8
mi_id = 10 ** 8

for idx,i in enumerate(H):
    idx += 1
    temp = T - (i * 0.006)
    
    n = abs(A - temp)
    
    if n < mi:
        mi = n
        mi_id = idx
print(mi_id)