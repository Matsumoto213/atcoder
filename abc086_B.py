import math
a,b = map(int, input().split())

ab = int(str(a)+str(b))


# abが平方数かどうか判定している
if math.sqrt(ab).is_integer() == True:
    print("Yes")
else:
    print("No")