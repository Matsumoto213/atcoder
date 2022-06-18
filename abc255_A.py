r,c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = [A] + [B]
print(L[r - 1][c - 1])