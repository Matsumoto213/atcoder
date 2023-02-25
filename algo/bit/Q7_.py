N,S = map(int, input().split())
Q = int(input())

for i in range(Q):
    a,b = map(int, input().split())
    if a == 0:
        # S の b 番目のビットを 1 にする
        S |= 1 << b
    elif a == 1:
        # S の b 番目のビットが 1 ならば on を、そうでないならば off を出力する
        if S & (1 << b):
            print("on")
        else:
            print("off")
