A,B = map(int, input().split())

ans = 0
cnt = 1

while cnt < B:
    cnt -= 1
    cnt += A
    ans += 1
print(ans)