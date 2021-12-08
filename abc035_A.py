W,H = map(int, input().split())
W4 = W % 16
H3 = H % 9
if W4 == H3 == 0:
    print("16:9")
else:
    print("4:3")