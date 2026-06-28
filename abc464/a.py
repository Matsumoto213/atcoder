S = input()

east = 0
west = 0

for i in range(len(S)):
    if S[i] == 'E':
        east += 1
    elif S[i] == 'W':
        west += 1

print('East' if east > west else 'West')