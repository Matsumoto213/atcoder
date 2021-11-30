# 基本の考え方としてどちらの判定の方が早いのかを咄嗟に考える

S = input()
T = input()

if S == "#." and T == ".#":
    print("No")
elif S == ".#" and T == "#.":
    print("No")
else:
    print("Yes")