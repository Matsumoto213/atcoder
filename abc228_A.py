S,T,X = map(int, input().split())

while True:
    if S == 25:
        S = 0
    
    if S == T:
        break
    
    if S == X:
        print("Yes")
        exit(0)
        
    S += 1
    
print("No")