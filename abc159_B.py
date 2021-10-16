s = input()
t = s[::-1]

if s == t:
    num = int((len(s) - 1) / 2)
    a = s[:num]
    number = int((len(s) + 3) / 2)
    b = s[number - 1:]
    if a == b:
        print("Yes")
        exit(0)
print("No")