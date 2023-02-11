s = input()

for i in range(len(s)):
    if s[i] == '0':
        print('1',end = "")
    elif s[i] == '1':
        print('0',end = "")
        