def I(): return input()

S = I()
AGCT = ['A', 'C', 'G', 'T']

ans = 0
max_ = 0
for i in range(len(S)):
    if S[i] in AGCT:
        max_ += 1
    else: 
        ans = max(ans, max_)
        max_ = 0
    
    if i == len(S) - 1:
        ans = max(ans, max_)
        
print(ans)