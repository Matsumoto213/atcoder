x = int(input())
leng = len(str(x))
if x % 10 != 0 and x < 0 and leng > 2:
    x = str(x)
    ans = int(x[:leng - 1]) - 1
    print(ans)
    exit(0)

x = str(x)
ans = str(x[:leng - 1])

if leng == 1 or (leng == 2 and int(x) < 0):
    ans = 0
print(ans)