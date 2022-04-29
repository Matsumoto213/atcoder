H,W = map(int,input().split())

mass = []


for i in range(H):
    m = list(input())
    mass.append(m)

if H == 1 and W >= 2:
    for i in range(H):
        for j in range(W):
            if mass[i][j] == '#':
                print('#',end = "")
                continue
            else:
                L = []
                if j == 0:
                    # 右のマス
                    L.append(mass[i][j + 1])
                elif j == W - 1:
                    # 左のマス
                    L.append(mass[i][j - 1])
                else:
                    # 右のマス
                    L.append(mass[i][j + 1])
                    # 左のマス
                    L.append(mass[i][j - 1])
                print(L.count('#'),end = "")
        exit()

if W == 1 and H >= 2:
    for i in range(H):
        for j in range(W):
            if mass[i][j] == '#':
                print('#',end = "")
                continue
            else:
                L = []
                if i == 0:
                    # 下のマス
                    L.append(mass[i + 1][j])
                elif i == H - 1:
                    # 上のマス
                    L.append(mass[i - 1][j])
                else:
                    # 下のマス
                    L.append(mass[i + 1][j])
                    # 上のマス
                    L.append(mass[i - 1][j])
            print(L.count('#'),end = "")
        print()
    exit()

if H == 1 and W == 1:
    if mass[0][0] == '#':
        print('#')
    else:
        print(0)
    exit()

for i in range(H):
    for j in range(W):
        if mass[i][j] == '#':
            print('#',end = "")
            continue
        else:
            L = []
            # 一番上の段の場合
            if i == 0:
                # 一番左の場合
                if j == 0:
                    # 右のマス
                    L.append(mass[i][j + 1])
                    # 右下のマス
                    L.append(mass[i + 1][j + 1])
                    # 下のマス
                    L.append(mass[i + 1][j])
                # 一番右の場合
                elif j == W - 1:
                    # 左のマス
                    L.append(mass[i][j - 1])
                    # 左下のマス
                    L.append(mass[i + 1][j - 1])
                    # 下のマス
                    L.append(mass[i + 1][j])
                # 真ん中に位置する場合
                else:
                    # 右のマス
                    L.append(mass[i][j + 1])
                    # 左のマス
                    L.append(mass[i][j - 1])
                    # 右下のマス
                    L.append(mass[i + 1][j + 1])
                    # 左下のマス
                    L.append(mass[i + 1][j - 1])
                    # 下のマス
                    L.append(mass[i + 1][j])
            # 一番下の場合
            elif i == H - 1:
                # 一番左の場合
                if j == 0:
                    # 右のマス
                    L.append(mass[i][j + 1])
                    # 右上のマス
                    L.append(mass[i - 1][j + 1])
                    # 上のマス
                    L.append(mass[i - 1][j])
                # 一番右の場合
                elif j == W - 1:
                    # 左のマス
                    L.append(mass[i][j - 1])
                    # 左上のマス
                    L.append(mass[i - 1][j - 1])
                    # 上のマス
                    L.append(mass[i - 1][j])
                # 真ん中に位置する場合
                else:
                    # 左のマス
                    L.append(mass[i][j - 1])
                    # 左上のマス
                    L.append(mass[i - 1][j - 1])
                    # 上のマス
                    L.append(mass[i - 1][j])
                    # 右上のマス
                    L.append(mass[i - 1][j + 1])
                    # 右のマス
                    L.append(mass[i][j + 1])
            # 一番上でも一番下でもない場合
            else:
                # 一番左の場合
                if j == 0:
                    # 上のマス
                    L.append(mass[i - 1][j])
                    # 右上のマス
                    L.append(mass[i - 1][j + 1])
                    # 右のマス
                    L.append(mass[i][j + 1])
                    # 右下のマス
                    L.append(mass[i + 1][j + 1])
                    # 下のマス
                    L.append(mass[i + 1][j])
                # 一番右の場合
                elif j == W - 1:
                    # 左のマス
                    L.append(mass[i][j - 1])
                    # 左上のマス
                    L.append(mass[i - 1][j - 1])
                    # 上のマス
                    L.append(mass[i - 1][j])
                    # 左下のマス
                    L.append(mass[i + 1][j - 1])
                    # 下のマス
                    L.append(mass[i + 1][j])
                # 真ん中に位置する場合
                else:
                    # 左のマス
                    L.append(mass[i][j - 1])
                    # 左上のマス
                    L.append(mass[i - 1][j - 1])
                    # 上のマス
                    L.append(mass[i - 1][j])
                    # 左下のマス
                    L.append(mass[i + 1][j - 1])
                    # 右上のマス
                    L.append(mass[i - 1][j + 1])
                    # 右のマス
                    L.append(mass[i][j + 1])
                    # 右下のマス
                    L.append(mass[i + 1][j + 1])
                    # 下のマス
                    L.append(mass[i + 1][j])
        print(L.count('#'),end = "")
    print()