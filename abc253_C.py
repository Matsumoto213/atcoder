Q = int(input())
S = []

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        S.append(int(query[1]))
    elif query[0] == '2':
        q = int(query[1])
        temp = min(S.count(q),q)
        cnt = 0
        for j in range(len(S)):
            if cnt == temp:
                break
            if S[j] == q:
                S.pop(q)
                cnt += 1
    else:
        print(max(S) - min(S))
