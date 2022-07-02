n,k = map(int, input().split())

def calc(n):
    n = list(str(n))
    n = [int(n[i]) for i in range(len(n))]
    n.sort()
    n = [str(i) for i in n]
    mi_ = "".join(n)
    ma_ = "".join(n[::-1])
    return int(ma_) - int(mi_)

for _ in range(k):
    n = calc(n)
print(n)