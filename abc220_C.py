n = int(input())

a = list(map(int, input().split()))
x = int(input())

goukei = sum(a)
ans = x // goukei
result = len(a) * ans
num = goukei * ans 

i = 0

while True:
    if num > x:
        break
    
    if i == len(a):
        i = 0
    
    result += a[i]
    result += 1
    i += 1
print(result)