# 割り算
# aはbで割り切れるかなど割り切れる計算の時にめちゃくちゃ使える
import math
a,b,c,d = map(int, input().split())

# 最小公倍数
temp = math.lcm(c,d)

a -= 1
ansb = b - (b // c + b // d - b // temp)
ansa = a - (a // c + a // d - a // temp)
print(ansb-ansa)