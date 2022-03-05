from collections import defaultdict
N = int(input())
cnt = dict(int)
for _ in range(N):
    st1 = list(input())
    st2 = ''.join(sorted(st1))
    cnt[st2] += 1

ans = 0

# 組みを求める場合はこのように2倍して1引いたものをかけそれから÷2をする
for bit in cnt.values():
    if bit >= 2:
        ans += bit * (bit - 1) // 2
print(ans)