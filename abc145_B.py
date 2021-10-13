n = int(input())
s = input()

if n % 2 == 0:
    num = n // 2
else:
    print("No")
    exit()
    
st = s[:num]*2

if s == st:
    print("Yes")
else:
    print("No")