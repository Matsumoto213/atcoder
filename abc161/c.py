N,K = map(int,input().split())
print(N % K,K - (N % K))
print(min(N % K,K - (N % K)))