n = int(input())
lst = list(map(int, input().split()))

if len(set(lst)) == n:
    print("YES")
else:
    print("NO")