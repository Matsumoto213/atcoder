n = input()

temp = 9 * len(n[1:])
# print(temp)

if len(n) == 1:
    ans = int(n)

elif n[0] != 9 and n[1:] != "9" * len(n[1:]):
    ans = temp + int(n[0]) - 1
else:
    ans = temp + int(n[0])
print(ans)
