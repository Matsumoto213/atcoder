N, K = map(int, input().split())
# グーで勝った場合:R
# チョキで勝った場合:S 
# パーで勝った場合:P
R,S,P = map(int, input().split())
T = input()
L = [''] * N

ans = 0
# rがグー sがチョキ　pはパー
for idx,i in enumerate(T):
    # グー
    if i == "r":
        if L[idx - K] == "P" and K <= idx:
            continue
        else:
            ans += P
            L[idx] = "P"
        
    # チョキ
    elif i == "s":
        if L[idx - K] == "R" and K <= idx:
            continue
        else:
            ans += R
            L[idx] = "R"
        
    # パー
    else:
        if L[idx - K] == "S" and K <= idx:
            continue
        else:
            ans += S
            L[idx] = "S"
print(ans)