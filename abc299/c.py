# 文字列 S の長さ N を使用して関数をテストします
N = int(input())
S = input()

def max_dango_level(N, S):
    max_level = -1
    count_o = 0

    for i in range(1, N):
        if S[i - 1] == '-' and S[i] == 'o':
            count_o = 1
        elif S[i - 1] == 'o' and S[i] == 'o':
            count_o += 1
        elif S[i - 1] == 'o' and S[i] == '-':
            max_level = max(max_level, count_o)
            count_o = 0

    return max_level


max_level = max_dango_level(N, S)
print(max_level)