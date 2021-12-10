S = input()
ans = ""

for i in S:
    if str.isdigit(i):
        ans = ans + str(i)
print(ans)
        