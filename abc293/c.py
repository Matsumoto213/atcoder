# 入力を受け取る
h, w = map(int, input().split())
a = [input().split() for _ in range(h)]

# 移動パターン (右または下) を事前に定義する
patterns = [(1, 0), (0, 1)]

def dfs(i, j, visited):
    # 終点に到達した場合、移動経路を含めた個数1で返す
    if i == h-1 and j == w-1:
        return 1

    # 次の移動先マスを訪れる
    count = 0
    for dx, dy in patterns:
        next_i, next_j = i + dx, j + dy

        # 移動先が存在し、まだ訪問していない場合
        if 0 <= next_i < h and 0 <= next_j < w and a[next_i][next_j] not in visited:
            visited.add(a[next_i][next_j]) # 訪問済みにする
            count += dfs(next_i, next_j, visited) # 次の移動先からの個数を数える
            visited.remove(a[next_i][next_j]) # 訪問済みから外す

    return count

# 始点から開始してdfsを呼び出す
visited = set([a[0][0]]) # 始点を訪問済みとする
result = dfs(0, 0, visited)

# 結果を出力する
print(result)
