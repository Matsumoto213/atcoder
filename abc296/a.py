def is_alternating(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True
N = int(input())
S = input()
result = is_alternating(S)
if result:
    print('Yes')
else:
    print('No')
