N,A,B = map(int, input().split())
dif = B - A

if dif % 2 == 0:
    print((B - A) // 2)
else:
    gather_1 = B - 1
    gather_N = N - A
    print(min(gather_1,gather_N))