N,M,H,K = map(int, input().split())
S = input()
items = [list(map(int, input().split())) for _ in range(M)]
def can_takahashi_survive(N, M, H, K, items, S):
    # 座標とアイテムの辞書を作成します。
    item_dict = {(x, y): True for x, y in items}

    # 高橋君の現在の座標を定義します。
    takahashi_position = [0, 0]

    # 各移動に対してループを回します。
    for i in range(N):
        if S[i] == 'R':
            takahashi_position[0] += 1
        elif S[i] == 'L':
            takahashi_position[0] -= 1
        elif S[i] == 'U':
            takahashi_position[1] += 1
        elif S[i] == 'D':
            takahashi_position[1] -= 1
        
        # 高橋君の体力を減らします。
        H -= 1
        
        # 高橋君の体力が負になった場合、彼は倒れてしまうので、Falseを返します。
        if H < 0:
            return False
        
        # 高橋君がアイテムのある場所に移動し、体力がK未満の場合、アイテムを取得します。
        if tuple(takahashi_position) in item_dict and H < K:
            H = K
            del item_dict[tuple(takahashi_position)]  # アイテムを取得したので、それを辞書から削除します。

    # N回の移動を終えて高橋君がまだ倒れていない場合、Trueを返します。
    return True

print('Yes' if can_takahashi_survive(N, M, H, K, items, S) else 'No')