a,b,h,m = map(int, input().split())
# もう一回やる
def findAngle(hh, mm):
    #は24時間表記を処理します
    hh = hh % 12
    #は時針の位置を見つけます
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)
    #は分の手の位置を見つけます
    m = (mm * 360) // (60)
    #は角度差を計算します
    angle = abs(h - m)
    #は短い角度を考慮して、それを返します
    if angle > 180:
        angle = 360 - angle
    return angle
import math
angle = findAngle(h,m)
radianA = math.radians(angle)
a_2 = a ** 2 + b ** 2 - (2 * a * b * math.cos(radianA))
ans = math.sqrt(a_2)
print(ans)