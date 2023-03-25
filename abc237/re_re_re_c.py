def longest_common_suffix(s, t):
    lcs = 0
    for i in range(min(len(s), len(t))):
        if s[-(i + 1)] == t[i]:
            lcs += 1
        else:
            break
    return lcs

def can_make_palindrome(s):
    reversed_s = s[::-1]
    lcs = longest_common_suffix(s, reversed_s)
    if lcs == len(s):
        return False, -1
    return True, len(s) - lcs

# 例を表示します
s = input()
result, num_a = can_make_palindrome(s)
if result:
    print("回文にできます")
    print(f"先頭に追加する 'a' の数: {num_a}")
else:
    print("回文にできません")
