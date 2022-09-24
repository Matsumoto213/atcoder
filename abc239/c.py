import math
x1,y1,x2,y2 = map(int, input().split())

# 右上
point1 = (x1 + 2,y1 + 1)

# 右上
point2 = (x1 + 1,y1 + 2)

# 右下
point3 = (x1 - 1,y1 + 2)

# 右下
point4 = (x1 - 2,y1 + 1)

# 左下
point5 = (x1 - 2,y1 - 1)

# 左下
point6 = (x1 - 1,y1 - 2)

# 左上
point7 = (x1 + 1,y1 - 2)

# 左上
point8 = (x1 + 2,y1 - 1)

P = [point1,point2,point3,point4,point5,point6,point7,point8]

def judgeExistsSqrt5(points,x,y):
    for i in range(len(points)):
        points[i] = list(points[i])
        temp = math.sqrt(((x - points[i][0]) ** 2) + ((y - points[i][1]) ** 2))
        if temp == math.sqrt(5):
            return True
    return False

if judgeExistsSqrt5(P,x1,y1) and judgeExistsSqrt5(P,x2,y2):
    print('Yes')
else:
    print('No')