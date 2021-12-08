S = input()
s = len(S)
t = len(set(S))

if s == t:
    print("yes")
else:
    print("no")