def linesearch(a,p):
    for i in range(0, len(a), 1):
        if a[i] == p:
            print("見つかりました"+str(i))
            break

a = [61,15,82,21,77,32,53]
p = 82
linesearch(a, p)