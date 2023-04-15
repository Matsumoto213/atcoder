N = int(input())
S = input()

judge = False

good = 0
bad = 0
usu = 0

for i in range(N):
    if S[i] == 'o':
        good += 1
    elif S[i] == 'x':
        bad += 1
    else:
        usu += 1

if good >= 1 and bad == 0:
    print('Yes')
else:
    print('No')