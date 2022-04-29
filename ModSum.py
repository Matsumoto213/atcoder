N = int(input())

def f(n):
    temp = 0
    for i in range(1,n + 1):
        temp += i
    return temp

print(f(N - 1))
