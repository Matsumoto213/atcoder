q,h,s,d = map(int, input().split())
n = int(input())


while True:
    if n == 0:
        break

    if n >= 2:
        ans += min(int(q*8),int(h*4),int(s*2),d)
        n -= 2
    else:
        ans += min(int(q*4),int(h*2),int(s*1))
        n -= 1
print(ans)



