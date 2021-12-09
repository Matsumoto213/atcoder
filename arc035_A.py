S = input()
T = S[::-1]
s = len(S)
s_symbol = []
t_symbol = []

for i,x in enumerate(S):
    if x == "*":
        s_symbol.append(i)
        t_symbol.append(len(S) - 1 - i)
t_symbol.sort()
      
if S == T or s == s_symbol:
    print("YES")
    exit(0)

if s_symbol == 0:
    if S != T:
        print("NO")
        exit(0)

S = list(S)
T = list(T)


for i in s_symbol:
    S[i:i + 1] = T[i]

for j in t_symbol:
    T[j:j + 1] = S[j]

if S == T:
    print("YES")
else:
    print("NO")
    