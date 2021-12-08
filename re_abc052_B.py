N = int(input())
S = input()

x = 0
ans = - 10 ** 8

for i in S:      
    if i == "I":
        x += 1
    else:
        x -= 1
    
    if x > ans:
        ans = x

if ans < 0:
    print(0)
else:
    print(ans) 