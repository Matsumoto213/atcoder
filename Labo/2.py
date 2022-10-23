ans = 0
for i in range(1,112):
    if i % 2 != 0:
        ans += i ** 3
    
print(ans)