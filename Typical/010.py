N = int(input())
one = [0]
two = [0]
for i in range(N):
    a,b = map(int, input().split())
    if a == 1:
        one.append(one[i] + b)
        two.append(two[i])
    elif a == 2:
        one.append(one[i])
        two.append(two[i] + b)

Q = int(input())
for i in range(Q):
    l,r = map(int, input().split())
    print(one[r] - one[l - 1], two[r] - two[l - 1])