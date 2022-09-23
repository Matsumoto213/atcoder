K = int(input())
# 2進数で表してから'1'を'2'に置き換えれば完了
s = str(format(K, 'b'))
temp = s.replace('1','2')
print(temp)