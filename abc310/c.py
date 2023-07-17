N = int(input())
S = [input() for _ in range(N)]
# 正転を消す
set_S = set(S)
S = list(set_S)
ans = 0
same = 0
for i in range(len(S)):
    reverse = S[i][::-1]
    if reverse not in set_S or len(reverse) == 1:
        ans += 1
    else:
        same += 1
print(ans + (same // 2))