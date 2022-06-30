S = input()
K = int(input())
ans = S.count('1')
if ans == len(S):
    print(1)
else:
    cnt = 0
    for ss in S:
        if ss == '1':
            cnt += 1
            if cnt >= K:
                print(1)
                exit()
        if ss != '1':
            print(ss)
            exit()