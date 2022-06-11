Q = int(input())
S = []

for i in range(Q):
    q = input().split()
    q = [int(n) for n in q]
    query = q[0]
    # 末尾に追加する
    if query == 1:
        S.append(q[1])

    # Sからxをmin(c,Sに含まれるxの個数)個を削除する
    elif query == 2:
        x = q[1]
        c = q[2]
        count = S.count(x)
        temp = min(c,count)
        cnt = 0
        # 削除する工程に入る
        for i in range(len(S)):
            if cnt < temp and S[i] == x:
                S.remove(x)
                cnt += 1
            else:
                continue
            if cnt >= temp:
                break
        # 最大値から最小値を引く
    else:
        print(max(S) - min(S))