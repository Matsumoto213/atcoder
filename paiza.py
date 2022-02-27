# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
X,Y,N = map(int, input().split())
D = [input() for _ in range(N)]
direction = "U"

for i in range(N):
    if D[i] == "L":
        if direction == "U":
            X -= 1
            direction = "L"
            print(X,Y)
        elif direction == "R":
            Y -= 1
            direction = "U"
            print(X,Y)
        elif direction == "D":
            X -= 1
            direction = "R"
            print(X,Y)
        elif direction == "L":
            Y += 1
            direction = "D"
            print(X,Y)
    else:
        if direction == "U":
            X += 1
            direction = "R"
            print(X,Y)
            
        elif direction == "R":
            Y += 1
            direction = "D"
            print(X,Y)
            
        elif direction == "D":
            X -= 1
            direction = "L"
            print(X,Y)
            
        elif direction == "L":
            Y -= 1
            direction = "U"
            print(X,Y)
            
            
        
    