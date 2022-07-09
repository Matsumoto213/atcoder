a,b,d = map(int,input().split())
import numpy as np
# 反時計回りに回転させる
deg45 = np.deg2rad(d)
cos = np.cos(deg45)
sin = np.sin(deg45)
x_dash = []
y_dash = []
rot_x = (a * cos) - (b * sin)
rot_y = (a * sin) + (b * cos)
    
print(rot_x,rot_y)