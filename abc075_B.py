H,W = map(int, input().split())
S = [input() for _ in range(H)]
lst = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            print("#",end = "")
        else:
            lst.clear()
            # 一番上の段
            if i == 0:
                # 一番左のマス
                if j == 0:
                    # 下のマス
                    lst.append(S[i + 1][j])
                    # 右のマス
                    lst.append(S[i][j + 1])
                    # 右下のマス
                    lst.append(S[i + 1][j + 1])
                # 一番右のマス
                elif j == W-1:
                    lst.append(S[i + 1][j])
                # 左のマス
                    lst.append(S[i][j - 1])
                # 左下のマス
                    lst.append(S[i + 1][j - 1])

                # 上記以外のマス
                else:
                    # 左
                    lst.append(S[i][j - 1])
                    # 左下
                    lst.append(S[i + 1][j - 1])
                    # 下
                    lst.append(S[i + 1][j])
                    # 右下
                    lst.append(S[i + 1][j + 1])
                    # 右
                    lst.append(S[i][j + 1])


            # 一番下のマス
            elif i == H - 1:
                # 一番左のマス
                if j == 0:
                    # 右
                    lst.append(S[i][j + 1])
                    # 右上
                    lst.append(S[i - 1][j + 1])
                    # 上
                    lst.append(S[i - 1][j])

                # 一番右のマス
                elif j == W - 1:
                    # 左
                    lst.append(S[i][j - 1])
                    # 左上
                    lst.append(S[i - 1][j - 1])
                    # 上
                    lst.append(S[i - 1][j])

                # 上記以外のマス
                else:
                    # 右
                    lst.append(S[i][j + 1])
                    # 右上
                    lst.append(S[i - 1][j + 1])
                    # 上
                    lst.append(S[i - 1][j])
                    # 左上
                    lst.append(S[i - 1][j - 1])
                    # 左
                    lst.append(S[i][j - 1])

            # 真ん中の列
            else:
                # 一番左のマス
                if j == 0:
                    # 右
                    lst.append(S[i][j + 1])
                    # 右上
                    lst.append(S[i - 1][j + 1])
                    # 上
                    lst.append(S[i - 1][j])
                    # 右下
                    lst.append(S[i + 1][j + 1])
                    # 下
                    lst.append(S[i + 1][j])


                # 一番右のマス
                elif j == W - 1:
                    # 左
                    lst.append(S[i][j - 1])
                    # 左上
                    lst.append(S[i - 1][j - 1])
                    # 上
                    lst.append(S[i - 1][j])
                    # 左下
                    lst.append(S[i + 1][j - 1])
                    # 下
                    lst.append(S[i + 1][j])

                # 上記以外のマス
                else:
                    # 左
                    lst.append(S[i][j - 1])
                    # 左上
                    lst.append(S[i - 1][j - 1])
                    # 上
                    lst.append(S[i - 1][j])
                    # 左下
                    lst.append(S[i + 1][j - 1])
                    # 下
                    lst.append(S[i + 1][j])
                    # 右
                    lst.append(S[i][j + 1])
                    # 右上
                    lst.append(S[i - 1][j + 1])
                    # 右下
                    lst.append(S[i + 1][j + 1])
            print(lst.count("#"),end = "")
    print()