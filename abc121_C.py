n,m = map(int, input().split())
dic = {}

 
for i in range(n):
    a,b = map(int, input().split())
    dic[a] = b
    
lst = sorted(dic.items())
dic.clear()
dic.update(lst)
 
price = 0

for key,counts in dic.items():
    if m >= counts:
        price += key * counts
        m -= counts
    else:
        price = key * m
        m = 0
        break
print(ans)