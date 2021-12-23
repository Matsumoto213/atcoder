# 素晴らしいコード
s = input()
lenS = len(s)

for i in range(lenS):
    for j in range(i,lenS):
        if 'keyence' == (s[:i] + s[j:]):
            print("YES")
            exit()
print("NO")