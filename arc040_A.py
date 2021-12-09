N = int(input())
R = 0
B = 0

for i in range(N):
    S = input()
    R += S.count("R")
    B += S.count("B")

if R > B:
    print("TAKAHASHI")
elif R < B:
    print("AOKI")
else:
    print("DRAW")