n = int(input())
lst = list(map(int, input().split()))
lst.sort()
# 偶数がeven 奇数がodd
odds = []
evens = []

for i in range(n):
    if lst[i] % 2 == 0:
        evens.append(lst[i])
    else:
        odds.append(lst[i])

while True:
    if len(odds) == 0 and len(evens) == 1 or len(odds) == 1 and len(evens) == 0:
        print("YES")
        break
    
    if len(odds) == 1 and len(evens) == 1:
        print("NO")
        break
    
    if len(evens) >= 2:
        ans = evens[0] + evens[1]
        evens.append(ans)
        del evens[0]
        del evens[1]
        
   
    
    if len(odds) >= 2:
        ans = odds[0] + odds[1]
        evens.append(ans)
        if len(odds) == 2:
            odds.clear()
        else:
            del odds[0]
            del odds[1]