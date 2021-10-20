s = input()
t = input()

if s == t:
  print("No")
  exit(0)

s = [s[i] for i in range(len(s))]
t = [t[i] for i in range(len(t))]

s.sort()
t.sort(reverse = True)

s = "".join(s)
t = "".join(t)

lst = [s,t]

lst.sort()

j = 0
for i in lst:
    if j == 0 and i == s:
        print("Yes")
        break
    else:
        print("No")
        break

