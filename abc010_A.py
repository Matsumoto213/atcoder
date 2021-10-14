n = int(input())
lst = list(map(int, input().split()))
lst.sort()


# 偶数がeven 奇数がodd
odds = []
evens = []

i = 0
while True: 
    if len(odds) == 0 and len(evens) == 2 or len(odds) == 2 and len(evens) == 0:
        print("YES")
        exit(0)
    
    if len(odds) == 1 and len(evens) == 1:
        print("NO")
        exit(1)

    
    if lst[i] % 2 == 0:
        evens.appen(i)
    else:
        odd.append(i)
    
    if len(evens) >= 2:
        ans = evens[0] + evens[1]
        odd.append(ans)
        del evens[0]
        del evens[1]
    
    if len(odds) >= 2:
        ans = odds[0] + evens[1]
        odd.append(ans)
        del odds[0]
        del odds[1]
        
    i += 1