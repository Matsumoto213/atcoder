o = input()
e = input()

ans = ''
oe = len(o) + len(e)
o_count = 0
e_count = 0

for i in range(oe):
    if i % 2 == 0:
        ans = ans+o[o_count]
        o_count += 1
    else:
        ans = ans+e[e_count]
        e_count += 1

print(ans)