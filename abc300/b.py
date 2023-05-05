H,W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

def grid_shift_match(A, B, H, W):
    for s in range(H):
        for t in range(W):
            is_match = True
            for i in range(H):
                for j in range(W):
                    # 縦方向のシフトをs回、横方向のシフトをt回行ったAの要素を計算
                    shifted_elem = A[(i-s) % H][(j-t) % W]
                    # シフト後のAとBが一致するかどうかを確認
                    if shifted_elem != B[i][j]:
                        is_match = False
                        break
                if not is_match:
                    break
            if is_match:
                return True
    return False

if grid_shift_match(A,B,H,W):
    print('Yes')
else:
    print('No')