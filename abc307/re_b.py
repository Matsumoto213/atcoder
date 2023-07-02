N = int(input())
S = [input() for _ in range(N)]

def is_palindrome(s):
    return s == s[::-1]

for i in range(N - 1):
    for j in range(i + 1, N):
        ans1 = S[i] + S[j]
        ans2 = S[j] + S[i]
        if is_palindrome(ans1) or is_palindrome(ans2):
            print('Yes')
            exit()
print('No')