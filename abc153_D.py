h = int(input())

ans = 0
count = 1 

while h > 0:
    ans += count
    h //= 2
    count *= 2
print(ans)


    
