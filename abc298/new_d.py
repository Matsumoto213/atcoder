mod = 998244353
S = '1'
q = int(input())

base = 1
tail = 0

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        x = query[1]
        S += x
        tail = (tail * 10 + int(x)) % mod
        base = (base * 10) % mod
    elif query[0] == '2':
        base = (base * pow(10, mod-2, mod)) % mod
        tail = (tail - int(S[0]) * base) % mod
        S = S[1:]
    elif query[0] == '3':
        print(tail)
