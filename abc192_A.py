x = input()

if len(x) == 1:
    print(100 - int(x))
    exit(0)

S = x[-2] + x[-1]
if S == '00':
    print(100)
else:
    temp = int(S)
    print(100 - temp)  

