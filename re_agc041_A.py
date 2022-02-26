N,A,B = map(int,input().split())

ab = A + B
if ab % 2 == 0:
    print(B - (B + A) // 2)
    exit()

go_one = B - 1
go_N = N - A
print(min(go_one,go_N))