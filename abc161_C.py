n, k = map(int, input().split())
print(n % k)
print(min(n%k,k - (n % k)))