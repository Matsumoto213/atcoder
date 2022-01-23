s = input()
q = int(input())

for _ in range(q):
    l = list(map(str, input().split())) 
    t = int(l[0])
    
    if t == 1:
        s = s[::-1]
    else:
        f = int(l[1])
        c = l[2]
        
        if f == 1:
            s = c + s
        else:
            s = s + c
            
print(s)
    
        
        