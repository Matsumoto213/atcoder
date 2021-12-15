N = int(input())
L = [i for i in range(1, N + 1)]
L.sort(reverse = True)
ans = 0

for idx,i in enumerate(L):
    idx += 1
    ans += idx % i
print(ans)