s = input() # 文字列を入力
t = "atcoder" # 目標とする文字列
n = len(s)
if n != len(t):
    print(-1) # 文字列の長さが異なる場合は-1を出力して終了
else:
    diff = 0
    for i in range(n):
        if s[i] != t[i]:
            diff += 1 # 文字列のi番目の文字が異なる場合はdiffを1増やす
    print(diff // 2) # 入れ替え操作は2文字ずつ行われるため、diffを2で割った整数部分が答え
