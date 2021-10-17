n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum_a = sum(a)
sum_b = sum(b)

if sum_a > sum_b:
    min_a = min(a)
    max_b = max(b)
    a.replace(min_a,max_b)
    print(sum(a))
else:
    min_b = min(b)
    max_a = max(a)
    b.replace(min_b,max_a)
    print(sum)



