S = input()
C = 10 ** 8
F = -10 ** 8

for idx,i in enumerate(S):
    if i == "C":
        C = min(C,idx)
    
    if i == "F":
        F = max(F,idx)
        

if C < F:
    print("Yes")
else:
    print("No")