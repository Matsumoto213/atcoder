import math
A,V = map(int, input().split())
B,W = map(int, input().split())
T = int(input())

if V <= W:
    print("NO")
elif A <= B and V <= W:
    print("NO")
else:
    dif = abs(V - W)
    dis = abs(B - A)
    
    ans = math.ceil(dis / dif)
    if ans <= T:
        print("YES")
    else:
        print("NO")