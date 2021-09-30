s = input()
n = len(s)

x = 0
y = 0
ans = []

for i in range(len(s)):
    if s[i] == "S":
        x += 1
        ans.append(s[i])
    elif s[i] == "N":
        x -= 1
        ans.append(s[i])
    elif s[i] == "E":
        y += 1
        ans.append(s[i])
    else:
        y -= 1
        ans.append(s[i])

ans = len(set(ans))

if x == 0 or y == 0:
    if ans % 2 == 0:
      print("Yes")
    else:
        print("No")