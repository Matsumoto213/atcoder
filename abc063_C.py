s = input()
s_len = len(s)
ans_len = len(set(s))

if s_len == ans_len:
    print("yes")
else:
    print("no")
