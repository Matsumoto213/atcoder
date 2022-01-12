from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
P = list(map(int, input().split()))
pq = P[:K]
heapify(pq)  # O(K)でリストpqをヒープ化と同時に0が最小になる（ソートしているわけではない）
print(pq[0])

# K以降の要素を追加していく中でK番目に大きい数を記述していくためにどうしているのか？
# heappushで要素を追加したのちにheappopで最小の値を捨てる
# その次に最小の値を出力する

for x in P[K:]:
    heappush(pq,x) # pqにxを追加する
    print(pq)
    heappop(pq) # 長さK + 1のリストpqで最小の値を捨てる
    print(pq[0])