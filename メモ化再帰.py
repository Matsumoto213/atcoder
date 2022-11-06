dict = {}

def function(n):
    if n == 0:
        return 1
    elif n in dict:
        return dict[n]
    else:
        if n not in dict:
            return function(n // 2) + function(n // 3)

N = int(input())
print(function(N))