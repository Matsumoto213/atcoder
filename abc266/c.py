ax,ay = map(int, input().split())
bx,by = map(int, input().split())
cx,cy = map(int, input().split())
dx,dy = map(int, input().split())

import numpy as np
import math

def is_over_180degrees(A, B):
    return A[0]*B[1] - A[1]*B[0]


a = np.array([ax,ay])
b = np.array([bx,by])
c = np.array([cx,cy])
d = np.array([dx,dy])

AB = [bx - ax, by - ay]
BC = [cx - bx, cy - by]
CD = [dx - cx, dy - cy]
DA = [ax - dx, ay - dy]
# aの角度
A = is_over_180degrees(AB,BC)


# # Bの角度
# vec3 = c - b
# vec4 = a - b
B = is_over_180degrees(BC,CD)

# # Cの角度
# vec5 = b - c
# vec6 = d - c
C = is_over_180degrees(CD,DA)

# # Dの角度
# vec7 = a - d
# vec8 = c - d
D = is_over_180degrees(DA,AB)

degree = [A,B,C,D]
for deg in degree:
    if deg < 0:
        print('No')
        exit()
print('Yes')