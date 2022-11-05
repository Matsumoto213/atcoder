S = input()
def ispalindrome(str): return 1 if str == str[::-1] else 0
for _ in range(1000):
    if ispalindrome(S):
        print('Yes')
        exit()
    else:
        S = 'a' + S
print('No')