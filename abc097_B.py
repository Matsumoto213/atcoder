x = int(input())
num = 0

for i in range(100):
    ans = i * i
    if x < ans:
        break
    num = max(ans,num)
print(num)