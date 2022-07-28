a,b,c,d = map(int, input().split())

dict = dict()

for i in range(0,101):
    dict[i] = 0

for i in range(a, b + 1):
    dict[i] += 1

for i in range(c, d + 1):
    dict[i] += 1

first = True
ans = 0
for key,value in dict.items():
    if value == 2 and first == True:
        first = False
        for i in range(key + 1, len(dict)):
            if dict[i] >= 2:
                ans += 1
            else:
                break
print(ans)