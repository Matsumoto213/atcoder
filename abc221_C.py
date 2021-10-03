n = sorted(input())[::-1]

# Nの先頭から奇数文字目からなる文字列を A、偶数文字目からなる文字列を B とする
a = n[0::2]
b = n[1::2]
print(a)
print(b)
ans_a = int("".join(a))
ans_b = int("".join(b))
print(ans_a * ans_b)