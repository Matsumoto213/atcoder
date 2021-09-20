n = int(input())
lst = list(map(int, input().split()))
lst.sort()

i = 0
while True:
    if i == len(lst):
        break
    if i == 0:
        if n == 2:
            ans = (lst[i] + lst[i + 1]) / 2
            break
        ans = (lst[i] + lst[i + 1]) / 2
        i += 2
    else:
        ans = (ans + lst[i]) / 2
        i += 1
    
print(ans)