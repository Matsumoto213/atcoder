s = input()
n = int(input())

if len(s) == 1:
    print(s)

i = 0
cnt = 0
while True:
    if i >= len(s):
        cnt += 1
        i = 0
    if cnt == n:
        break
    if s[i] == '1':
        s = s[:i]+'1'+ s[i + 1:]
        i += 1

    elif s[i] == '2':
        s = s[:i] + '2' * 2 + s[i + 1:] 
        i += 2

    elif s[i] == '3':
        s = s[:i] + '3' * 3 + s[i + 1:] 
        i += 3

    elif s[i] == '4':
        s = s[:i]+'4'*4 +s[i + 1:] 
        i += 4

    elif s[i] == '5':
        s = s[:i] + '5' * 5 + s[i + 1:] 
        i += 5
    elif s[i] == '6':
        s = s[:i] + '6' * 6 + s[i + 1:] 
        i += 6
    elif s[i] == '7':
        s = s[:i] + '7' * 7 + s[i + 1:] 
        i += 7
    elif s[i] == '8':
        s = s[:i] + '8' * 8 + s[i + 1:] 
        i += 8
    else:
        s = s[:i] + '9' * 9 + s[i + 1:] 
        i += 9

print(s[n - 1])