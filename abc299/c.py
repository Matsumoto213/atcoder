def max_dango_level(N, S):
    max_level = -1

    for i in range(N - 1):
        if S[i] == 'o' and S[i + 1] == '-':
            current_level = 1
            j = i + 2
            while j < N - 1 and S[j] == 'o' and S[j + 1] == '-':
                current_level += 1
                j += 2
            max_level = max(max_level, current_level)

    return max_level


# 文字列 S の長さ N を使用して関数をテストします
N = int(input())
S = input()

max_level = max_dango_level(N, S)
print(max_level)
