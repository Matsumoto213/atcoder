N = int(input())
W = input().split()
ans = ['and','not','that','the','you']


for i in range(N):
    if W[i] in ans:
        print('Yes')
        exit()
print('No')