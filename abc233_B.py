L,R = map(int, input().split())
S = input()
S = list(S)

s = S[L - 1:R]
s = s[::-1]
S[L - 1:R] = s

print(''.join(S))