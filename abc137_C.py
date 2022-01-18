from collections import defaultdict
N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    st1 = list(input())
    st2 = ''.join(sorted(st1))
    cnt[st2] += 1

ans = 0

for bit in cnt.values():
    if bit >= 2:
        ans += bit * (bit - 1) // 2
print(ans)