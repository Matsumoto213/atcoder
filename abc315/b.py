M = int(input())
D = list(map(int, input().split()))

def find_middle_day(M, D):
    # 全体の日数を計算します
    total_days = sum(D)
    # 中心の日を求めます
    mid_day = (total_days + 1) // 2
    
    accumulated_days = 0
    for i in range(M):
        accumulated_days += D[i]
        if accumulated_days >= mid_day:
            return i + 1, mid_day - (accumulated_days - D[i])

# 結果を計算し、出力します
month, day = find_middle_day(M, D)
print(month, day)