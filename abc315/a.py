S = input()
L = ['a','e','i','u','o']
for i in range(len(S)):
    if S[i] not in L:
        print(S[i], end = "")
print()