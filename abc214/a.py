n = int(input())
if 1 <= n <= 125:
    cnt = 4
elif 126 <= n <= 211:
    cnt = 6
elif 212 <= n <= 214:
    cnt = 8
print(cnt)