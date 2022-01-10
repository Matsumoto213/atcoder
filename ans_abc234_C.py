K = int(input())
# Kの2進数表記
b = format(K, 'b')
print(b)
ans = b.replace('1', '2') # str型であるbの'1'を'2'に置き換えます
print(ans)