N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxIndex = [i + 1 for i, x in enumerate(A) if x == max(A)]

for i in maxIndex:
    if i in B:
        print("Yes")
        exit()
print("No")