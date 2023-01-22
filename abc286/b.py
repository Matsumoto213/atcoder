N = int(input())
S = input()
ans = ''
idx = 0
while True:
    if idx - 2 >= N:
        break
    if S[idx] + S[idx + 1] == 'na':
        idx += 1
        ans += 'nya'
    else:
        ans += S[idx]
    idx += 1
    print(idx)