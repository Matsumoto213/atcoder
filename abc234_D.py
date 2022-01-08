N,K = map(int, input().split())
p = list(map(int, input().split()))


for i in range(N - K + 1):
    temp = p[:K + i]
    temp.sort(reverse = True)
    print(temp[K - 1])