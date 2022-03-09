a,b,c = map(int, input().split())
from decimal import Decimal
AB = Decimal(a)**Decimal('0.5') + Decimal(b)**Decimal('0.5')
C = Decimal(c)**Decimal('0.5')
print('Yes' if AB < C else 'No')