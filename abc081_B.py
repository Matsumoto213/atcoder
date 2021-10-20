n = int(input())
a = list(map(int, input().split()))

even = True

i = 0
cnt = 0

while True:
    if even == False:
        break
    if i == len(a):
        cnt += 1
        i = 0
    
    if a[i] % 2 == 0:
        a[i] /= 2
    else:
        even = False
    i += 1
print(cnt)