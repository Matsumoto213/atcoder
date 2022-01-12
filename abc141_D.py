import heapq
n, m = map(int, input().split())

# 全ての値に-をつける
a = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(a)

# 判断するのが最小の値だけでいい時かつ計算量を少なくしたいときに使う
for _ in range(m):
    tmp_min = heapq.heappop(a)
    heapq.heappush(a, (-1) * (-tmp_min // 2))
    print(a)
# print(-sum(a))

