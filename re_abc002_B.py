S = input()
L = ["a","i","u","e","o"]

ans = ""

for i in S:
    if i not in L:
        ans = ans + i
print(ans)