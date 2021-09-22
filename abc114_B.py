s = input()

ans = 10 ** 8

for i in range(len(s) - 2):
    num = abs(753 - int(s[i:i+2]))
    ans = min(num,ans)
print(ans)

    
