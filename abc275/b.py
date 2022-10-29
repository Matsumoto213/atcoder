a,b,c,d,e,f = map(int, input().split())

abc = a * b * c
de = d * e * f

print((abc - de) % 998244353)