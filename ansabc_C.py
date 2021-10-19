s=input()
k=int(input())
idx=0
ans=0
while True:
    if idx==len(s):
        break
    if s[idx]=='1':
        idx=idx+1
    else:
        ans=s[idx]
        break

if idx >= k:
    print(1)
else:
    print(ans)
