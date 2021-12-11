N = int(input())
n = len(str(N))   
if n > 3 and n < 7:
    print(N - 1000 + 1)
elif n >= 7 and n < 10:
    print((N - 999999) + 999001)
elif n >= 10 and n < 13:
    print((N - 999999999) + 999999001)
elif n >= 13 and n < 16:
    print((N - 999999999999) + 1)
else:
    print((N - 999999999999999)
