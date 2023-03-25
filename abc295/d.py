S = input()

def count_happy_strings(S):
    n = len(S)
    count = 0
    freq_diff = [[0] * 10 for _ in range(n)]

    for r in range(n):
        digit = int(S[r])
        for d in range(10):
            if r > 0:
                freq_diff[r][d] = freq_diff[r-1][d]
            if d == digit:
                freq_diff[r][d] += 1

        even_freq_diff = all(freq_diff[r][d] % 2 == 0 for d in range(10))
        even_last_pos = all(i % 2 == 0 for i in freq_diff[r] if i > 0)
        if even_freq_diff and even_last_pos:
            count += 1

    return count

result = count_happy_strings(S)
print(result)