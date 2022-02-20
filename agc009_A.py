N = int(input())

a = []
b = []

for i in range(N):
    A,B = map(int, input().split())
    a.append(A)
    b.append(B)

a = a[::-1]
b = b[::-1]

temp = 0
for i in range(len(a)):
    a[i] += temp
    if a[i] % b[i] != 0:
        if a[i] < b[i]:
            temp += abs(a[i] - b[i])
        else:
            temp += b[i] * (a[i] // b[i] + 1) - a[i]
print(temp)