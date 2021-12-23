H,W = map(int, input().split())

h = []
w = []

M = []

for i in range(H):
    mass = input()
    
    # Mにmassを入れる
    M.append(mass)
    
    # .の数を数え、それがWと同じであればスルーしたいのでスルーリストに追加する
    count_w = mass.count(".")
    if count_w == W:
        w.append(i)

for i in range(W):
    count_h = 0
    for j in range(H):
        if M[j][i] == ".":
            count_h += 1
    if count_h == H:
        h.append(i)


for i in range(H):
    ans = []
    for j in range(W):
        if j in h or i in w:
            continue
        else:
            ans.append(M[i][j])
        print("".join(ans))