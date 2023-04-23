N = int(input())
S = input()
if 'o' in S and '-' in S:
    print(max(map(len, S.split('-'))))
else:
    print(-1)