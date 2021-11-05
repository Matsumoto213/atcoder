S = input()
ans = []

for i in S:
    if i != "a" and i != "i" and i != "u" and i != "e" and i != "o":
        ans.append(i)
result = "".join(ans)
print(result)