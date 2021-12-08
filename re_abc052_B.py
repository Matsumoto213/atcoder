N = int(input())
S = input()

x = 0
ans = - 10 ** 8

for i in S:
    if x > ans:
        ans = x
            
    if i == "I":
        x += 1
    else:
        x -= 1
print(ans)
        