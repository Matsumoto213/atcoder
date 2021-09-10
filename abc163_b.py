n,m = map(int, input().split())

# 夏休みの宿題m個, 夏休みはn日間
# 遊べる日にちを出力、ない場合は-1を出力

homework = list(map(int, input().split()))

for i in range(len(homework)):
    n -= homework[i]

if n < 0:
    print(-1)
else:
    print(n)