N,A,B = map(int, input().split())
S = input()
ab = A + B
Pass = 0
abroad = 0
for i in range(N):
    if S[i]== 'c':
        print('No')
    elif S[i] == 'b':
        # 海外の学生は予選通過車がA + B以下でかつ海外の学生の中での順がB位いないであれば通過
        if Pass < ab and abroad < B:
            Pass += 1
            abroad += 1
            print('Yes')
        else:
            print('No')
    else:
        if Pass < ab:
            Pass += 1
            print('Yes')
        else:
            print('No')