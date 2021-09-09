n = int(input())
montain = {}

for i in range(n):
    s1,t1 = map(str, input().split())
    t1 = int(t1)
    montain[t1] = s1
montain_name = sorted(montain.items(),reverse = True)

for i in range(len(montain_name)):
    for meter, name in montain_name.items():
        if i == 1:
            print(name)


