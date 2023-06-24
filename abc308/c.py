Ha,Wa = map(int, input().split())
A = [input() for _ in range(Ha)]
Hb,Wb = map(int, input().split())
B = [input() for _ in range(Hb)]
Hx,Wx = map(int, input().split())
X = [input() for _ in range(Hx)]

def can_form_sheet(h_a, w_a, sheet_a, h_b, w_b, sheet_b, h_x, w_x, sheet_x):
    max_h = max(h_a, h_b, h_x) * 2
    max_w = max(w_a, w_b, w_x) * 2
    sheet_c = [['.' for _ in range(max_w)] for _ in range(max_h)]

    # シートAをシートCの中央に配置
    start_a_h, start_a_w = max_h//2 - h_a//2, max_w//2 - w_a//2
    for i in range(h_a):
        for j in range(w_a):
            if sheet_a[i][j] == '#':
                sheet_c[start_a_h+i][start_a_w+j] = '#'

    # シートBをシートCの各位置に配置し、その度にシートXと一致するか確認
    for start_b_h in range(max_h - h_b + 1):
        for start_b_w in range(max_w - w_b + 1):
            # シートBの配置
            for i in range(h_b):
                for j in range(w_b):
                    if sheet_b[i][j] == '#':
                        sheet_c[start_b_h+i][start_b_w+j] = '#'

            # シートCからシートXと同じサイズの領域を切り出し、シートXと比較
            for i in range(max_h - h_x + 1):
                for j in range(max_w - w_x + 1):
                    matched = all(sheet_c[i+dx][j+dy] == sheet_x[dx][dy] for dx in range(h_x) for dy in range(w_x))
                    if matched:
                        return True

            # シートBを削除
            for i in range(h_b):
                for j in range(w_b):
                    if sheet_b[i][j] == '#':
                        sheet_c[start_b_h+i][start_b_w+j] = '.'

    return False

print(can_form_sheet(Ha,Wa,A,Hb,Wb,B,Hx,Wx,X))