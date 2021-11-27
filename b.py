a,b = map(str, input().split())
max_len = int(-min(len(a), len(b)))
max_len= -max_len


for i in range(-1,max_len - 1,-1):
    ans = int(a[i]) + int(b[i])
    if ans > 9:
        print("Hard")
        exit(0)
print("Easy")