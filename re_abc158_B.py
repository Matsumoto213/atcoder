N,A,B = map(int, input().split())

AB = A + B
if A == 0:
    print(0)
    exit(0)

group = N // AB
mass = AB * group
nod = N - mass

# if nod >= A:
#     print((A * group) + nod - A)
# else:
#     print((A * group) + nod)
    
if nod <= A:
    print((A * group) + nod)
else:
    print((A * group) + nod - A)
    