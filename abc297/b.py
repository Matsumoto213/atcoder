S = input()

guu = False
kisuu = False
for i in range(len(S)):
    if S[i] == 'B':
        if i % 2 != 0:
            guu = True
        else:
            kisuu = True

R = False
K = False
for i in range(len(S)):
    if S[i] == 'R':
        if R:
            R = False
        else:
            R = True
    
    if S[i] == 'K' and R == True:
        K = True

if K and guu and kisuu:
    print('Yes')
else:
    print('No')