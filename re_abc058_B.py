O = input()
E = input()
e = 0
for i in range(len(O + E)):
    if i % 2 == 0:
        e += 1
        print(E[e],end = "")
    else:
        o += 1
        print(O[o],end = "")
        
        
    
    