N = int(input())
S = [input() for _ in range(N)]

def is_palindrome(s):
    return s == s[::-1]

def check_palindrome_pairs(strings):
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_palindrome(strings[i] + strings[j]) or is_palindrome(strings[j] + strings[i]):
                return True
    return False


print('Yes' if check_palindrome_pairs(S) else 'No')