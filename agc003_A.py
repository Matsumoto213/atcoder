s = input()
N = 0
W = 0
S = 0
E = 0

for i in s:
    if i == "W":
        W += 1
    elif i == "N":
        N += 1
    elif i == "S":
        S += 1
    else:
        E += 1

if (N != 0 and S == 0) or (S != 0 and N == 0):
    print("No")
    exit()

elif (W != 0 and E == 0) or (E != 0 and W == 0):
    print("No")
    exit()
print("Yes")