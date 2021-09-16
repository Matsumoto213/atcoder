n = int(input())
t,a = map(int,input().split())
place = list(map(int,input().split()))
ans = []
 
for i in place:
    tem = t - i * 0.006
    temp = abs(tem - a)
    ans.append(temp)
 
min_value = min(ans)
min_index = ans.index(min_value) + 1
print(min_index)