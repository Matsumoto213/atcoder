s = '0123456789'
S = input()


for i in range(len(S) + 1):
    if s[i] not in S:
        print(s[i])
        exit()