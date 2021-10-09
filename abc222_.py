n = input()

ans = 4 - len(n)


if len(n) != 4:
    n = "0"*ans + n
    
print(n)