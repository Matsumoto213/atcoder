S = input()
T = 'oxxoxxoxxo'

for i in range(len(S)):
    if len(S) == 1:
        break
    if T[:len(S)] == S:
        print('Yes')
        exit()
    else:
        S = S[1:]
print('No')