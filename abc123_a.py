a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

ans = True
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        result = abs(lst[i] - lst[j])
        if result > k:
            ans = False
            break

if ans:
    print("Yay!")
else:
    print(":(")