n = int(input())
a = int(input())
num = 0

if n > 500:
    ans = n // 500
    num = ans * 500

if num + a < n:
    print("Yes")
else:
    print("No")



