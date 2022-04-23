S = input()
l = len(S)
le = len(set(S))

komozi = False
oomozi = False

for i in S:
    if i.islower():
        komozi = True
    elif i.isupper():
        oomozi = True

if l == le and komozi and oomozi:
    print('Yes')
else:
    print('No')