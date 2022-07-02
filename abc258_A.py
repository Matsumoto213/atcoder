N = int(input())

if N >= 60:
    N = N - 60
    if N <= 9:
        print('22:0'+str(N))
    else:
        print('22:'+str(N))
else:
    if N <= 9:
        print('21:0'+str(N))
    else:
        print('21:'+str(N))