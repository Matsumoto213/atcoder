A = int(input())

for i in range(1,101):
    ans = i ** 3
    if ans == A:
        print("YES")
        exit(0)
print("NO")