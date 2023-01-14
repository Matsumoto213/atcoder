def can_make_palindrome(s):
    for i in range(len(s)+1):
        if s == 'a'*i+s[:i:-1]:
            return True
    return False

s = input()
print(can_make_palindrome(s))