h, w = map(int,input().split())

for i in range(h):
    if i == 0:
        print("#"*(w + 2))
        
    p = input()
    print("#"+ p + "#")

    if i == h - 1:
        print("#"*(w + 2))

            
            