K,A,B = map(int,input().split())

bis = 1

while K > 0:
    temp = abs(A - bis + 2)
    dis = B - A
    # 残りの回数でビスケットがAまでとどき、B円に変換できる場合
    if K >= temp and dis >= 2:
        K -= temp
        bis += abs(A - bis)
        bis -= A
        bis += B
    # 届かない場合
    else:
        bis += K
        K = 0
print(bis)