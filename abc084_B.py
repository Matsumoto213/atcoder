a,b = map(int, input().split())
s = input()

ans = False

result = s[a]

s = s[:a]+s[a + 1:]

if result == "-" and s.isdigit():
    ans = True

if ans:
    print("Yes")
else:
    print("No")
