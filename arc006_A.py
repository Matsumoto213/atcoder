N = int(input())
s = input()
t = input()
cnt = N

for i in range(N):
    if s[i:] == t[:N - i]:
        cnt = i
        break
print(N + cnt)
