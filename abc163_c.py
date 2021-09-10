n = int(input())
# 各社員
# 社員番号位の社員以外のsyベテの社員には社員番号が自分より小さい上司が一人いる
lst = list(map(int, input().split()))
ans = {}

for i in range(1,n + 1):
    ans[i] = 0

for j in lst:
    ans[j] += 1

for value in ans.values():
    print(value)