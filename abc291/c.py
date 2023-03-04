N = int(input())
S = input()
x,y = 0,0
g = {(x,y)}

for i in range(N):
    if S[i] == 'R':
        x += 1
    elif S[i] == 'L':
        x -= 1
    elif S[i] == 'U':
        y += 1
    elif S[i] == 'D':
        y -= 1
    
    # tupleにリストを追加していく
    now = tuple((x,y))
    if now in g:
        print('Yes')
        exit()
    else:
        g.add(now)

print('No')