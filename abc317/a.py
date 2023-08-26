N,H,X = map(int, input().split())
P = list(map(int, input().split()))

# 目標の体力差を計算
diff = X - H

# 効き目の弱い傷薬から順に目標の体力差以上の効果があるか確認
for i in range(N):
    if P[i] >= diff:
        print(i + 1)  # 1-indexed なので +1 して出力
        break