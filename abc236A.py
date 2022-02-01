S = input()
a,b = map(int,input().split())

for i,key in enumerate(S):
    i += 1
    if i == a:
        print(S[b - 1],end = "")
    elif i == b:
        print(S[a - 1], end= "")
    else:
        print(key,end = "")
print()
