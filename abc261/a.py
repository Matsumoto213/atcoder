a,b,c,d = map(int, input().split())
dct = {}
for i in range(102):
    dct[i] = 0

for i in range(a, b + 1):
    dct[i] += 1

for i in range(c, d + 1):
    dct[i] += 1

judge = False
ans = 0
for key,value in dct.items():
    if value >= 2 and judge == False:
        judge = True
        for j in range(key + 1, len(dct) + 1):
            if dct[j] >= 2:
                ans += 1
            else:
                break
print(ans)