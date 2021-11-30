import collections
S = input()

S = collections.Counter(S)
S = S.keys()
T = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(T)):
    if T[i] not in S:
        print(T[i])
        exit(0)
print("None")