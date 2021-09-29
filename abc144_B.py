n = int(input())
ans = False

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result == n:
            ans = True
if ans:
  print("Yes")
else:
  print("No")