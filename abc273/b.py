x,k = map(int, input().split())
from decimal import Decimal, ROUND_HALF_UP
# 整数を任意の桁数で四捨五入（厳密）
for i in range(1,k + 1):
    x = int(Decimal(x).quantize(Decimal('1E'+str(i)), rounding=ROUND_HALF_UP))
print(x)