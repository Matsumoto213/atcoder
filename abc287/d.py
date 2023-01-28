s = input()
t = input()

for x in range(len(s)-len(t)+1):
    match = True
    for i in range(len(t)):
        if (s[x+i] != t[i]) and (s[x+i] != '?') and (t[i] != '?'):
            match = False
            break
    if match:
        print("Yes")
    else:
        print("No")
