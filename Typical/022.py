a,b,c = map(int,input().split())

def min_cuts(a, b, c):
    # 幅、奥行き、高さを昇順にソート
    a, b, c = sorted([a, b, c])

    # 全てのピースを立方体にするための最小の操作数を計算
    if a == b == c:
        # すでに立方体である場合、操作は不要
        return 0
    elif a == b:
        # 高さ方向に1回操作を行い、残りの2つの面が正方形になるように切断する
        return 1 + min_cuts(a, b, c - a)
    elif b == c:
        # 幅方向に1回操作を行い、残りの2つの面が正方形になるように切断する
        return 1 + min_cuts(a, b - a, c)
    else:
        # 幅方向、奥行き方向、高さ方向のどれか1つの方向に操作を行う
        return 1 + min(min_cuts(a, b - a, c - a), min_cuts(a - b, b, c - b), min_cuts(a - c, b - c, c))


print(min_cuts(a,b,c))