N = int(input())
if N >= 42:
    print('AGC0' + str(N + 1))
elif N <= 9:
    print('AGC00'+str(N))
else:
    print('AGC0' + str(N))