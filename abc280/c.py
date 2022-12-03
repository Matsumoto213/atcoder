S = input()
T = input()
for i in range(len(T)):
    if i >= len(S):
        print(len(T))
        exit()

    if S[i] != T[i]:
        print(i + 1)
        exit()