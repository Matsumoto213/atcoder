H, W = map(int, input().split())
a = [input() for _ in range(H)]

i_list = []
for i in range(H):
  if "#" in a[i]:
    i_list.append(i)

j_list = []

# 表を縦に見るときにめちゃくちゃ便利
for j, chars in enumerate(zip(*a)):
  if "#" in chars:
    j_list.append(j)

for i in i_list:
  row_chars = ""
  for j in j_list:
    row_chars += a[i][j]
  print(row_chars)
