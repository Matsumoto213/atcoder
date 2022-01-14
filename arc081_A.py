from collections import Counter
N = int(input())
a = list(map(int, input().split()))

# 2回以上の中で大きい二つを探す
C = Counter(a)
x = sorted(C.items(),reverse = True)

W = 0
H = 0

w_bool = False
h_bool = False
for key,value in x:

    if value >= 2 and w_bool == False:
        W = key
        value -= 2
        w_bool = True
        
        if value >= 2 and w_bool == True:
            H = key
            h_bool = True
            break
    if w_bool == True and h_bool == False and value >= 2:
        H = key
        h_bool = True
        break
    
print(W * H)
    
            
        
    