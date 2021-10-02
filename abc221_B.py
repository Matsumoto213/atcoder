s = input()
t = input()


if s == t:
    print("Yes")
    exit(0)

s = list(s)

for i in range(len(s) - 1):
    s[i], s[i + 1] = s[i + 1], s[i]
    ans = "".join(s)
    if ans == t:
        print("Yes")
        exit(0)
    else:
        s[i + 1], s[i] = s[i], s[i + 1]
print("No")