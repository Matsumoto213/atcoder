H,W = map(int, input().split())
a = [input() for _ in range(H)]

w = []
for i in range(H):
  if "#" in a[i]:
    w.append(i)

h = []
# 縦のマスを見るときにとても最適
for j, chars in enumerate(zip(*a)):
    if "#" in chars:
        h.append(j)

for i in w:
    for j in h:
        print(a[i][j],end="")
    print()
        
        