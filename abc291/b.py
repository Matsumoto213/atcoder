N = int(input())
x = list(map(int,input().split()))
x.sort(reverse = True)
temp = sum(x) - (sum(x[:N]) + sum(x[- N:]))
print(temp / (len(x) - (N * 2)))