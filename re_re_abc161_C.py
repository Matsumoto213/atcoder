N,K = map(int, input().split())
temp = N % K
print(min(temp,abs(temp - K)))