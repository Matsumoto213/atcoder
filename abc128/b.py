N = int(input())

L = []
for i in range(N):
    S,P = input().split()
    P = int(P)
    L.append([S,-P,i + 1])
sorted_data = sorted(L, key=lambda x:(x[0], x[1]))

for i in range(N):
    print(sorted_data[i][2])