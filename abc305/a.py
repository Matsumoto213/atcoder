N = int(input())
ans = N % 5
if ans < 3:
    print(N // 5 * 5)
else:
    print(N // 5 * 5 + 5)