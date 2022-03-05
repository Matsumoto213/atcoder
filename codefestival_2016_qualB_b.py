N,A,B = map(int, input().split())
S = input()

a = 0
b = 0
passing = 0

for i in range(len(S)):
    if S[i] == 'c':
        print('No')
    elif S[i] == 'a':
        if passing < A + B:
            print('Yes')
            passing += 1
        else:
            print('No')
    else:
        if passing < A + B and b < B:
            print('Yes')
            b += 1
            passing += 1
        else:
            print('No')