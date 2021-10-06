s = input()
s = [i for i in s]
s = len(set(s))

if s == 1:
    print("Won")
else:
    print("Lost")