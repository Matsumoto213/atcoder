n = int(input())
a = list(map(int, input().split()))
lst = []

i = 1
ans = 0
for j in a:
    string = str(i)+str(j)
    reverse_s = str(j)+str(i)
    if string not in lst and reverse_s not in lst:
        lst.append(string)
    else:
        ans += 1
    i += 1
print(ans)



