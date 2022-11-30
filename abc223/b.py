s = input()
L = []

for _ in range(len(s)):
    L.append(s)
    s = s[1:] + s[0]

L.sort(reverse = True)
print(L[-1])
print(L[0])