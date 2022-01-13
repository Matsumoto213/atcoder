from collections import Counter
s = input()
n = len(s)

C = Counter(s)
temp = C.most_common()[0]

max_s = temp[0]
max_ = temp[1]
tmp = 0

if len(set(s)) <= 2 and n >= 3:
    print("NO")
    exit(0)
    
for i in range(1,n + 1,3):
    tmp += 1
    
if max_ == tmp:
    print("YES")
else:
    print("NO")
    