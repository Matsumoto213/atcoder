H,W = map(int, input().split())
C = [input() for _ in range(H)]

for chars in zip(*C):
    print(chars.count("#"),end = " ")