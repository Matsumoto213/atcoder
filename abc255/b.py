N,K = map(int, input().split())
A = list(map(int, input().split()))
import numpy as np
l = []
for _ in range(N):
    x,y = map(int, input().split())
    l.append([x,y])

ans = []


def compTwoDigit(a,b):
    if (a[0] > 0 and a[1] < 0 and b[0] > 0 and b[1] < 0) or (a[0] > 0 and a[1] < 0 and b[0] < 0 and b[1] > 0) or (a[0] < 0 and a[1] > 0 and b[0] < 0 and b[1] > 0) or (a[0] < 0 and a[1] > 0 and b[0] > 0 and b[1] < 0):
        return True
    else:
        return False

# 全ての人が明るくなるのに必要な灯りの強さを求める。
for i in A:
    for j in range(N):
        j += 1
        if i == j or j in A:
            continue
        else:
            x = np.array([l[i - 1][0], l[j - 1][0]])
            y = np.array([l[i - 1][1], l[j - 1][1]])
            if compTwoDigit(x,y):
                ans.append(np.linalg.norm(x+y))
            else:
                ans.append(np.linalg.norm(x-y))
print(max(ans))
