N = int(input())
  
for i in range(N,0,-1):
    if (i ** .5).is_integer():
        print(i)
        exit(0)