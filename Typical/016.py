N = int(input())
a,b,c = map(int, input().split())
ans = 10000
for x in range(10000):
    for y in range(10000):
        value = x * a + y * b
        if value % c != 0 or value > N:
            continue
        z = (N - value) // c
        if ans > x + y + z:
            ans = x + y + z
print(ans)