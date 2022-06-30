from decimal import Decimal
a,b,c = map(str, input().split())

print('Yes' if Decimal(a)**Decimal('0.5') + Decimal(b)**Decimal('0.5') < Decimal(c)**Decimal('0.5') else 'No')