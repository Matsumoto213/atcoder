S = input()
cnt = 0
while(1):
    if S == S[::-1]:
        print('Yes')
    else:
        S = 'a' + S
    cnt += 1
    if cnt >= 100000:
        print('No')
        exit()
        