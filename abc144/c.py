N = int(input())

# 階乗の-1までループする。
def solution(n):
    temp = 0
    for i in range(n):
        if i * i > n:
            break
        else:
            temp = i
    return temp

ans = 10 ** 15 + 9
for i in range(1,solution(N) + 1):
    if N % i == 0:
        ans = min(ans,(i - 1) + (N // i - 1))
print(ans)

