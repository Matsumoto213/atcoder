s = input()
ans = int(1e9 + 7)

def solve(c):
    t = s
    cnt = 0
    while True:
        if len(set(t)) == 1:
            return cnt
        
        m = []
        for i in range(len(t) - 1):
            if t[i] == c or t[i + 1] == c:
                m.append(c)
            else:
                m.append(t[i])
        t = "".join(m)
        cnt += 1

# 実引数にa ~ zまで代入していく
for i in range(26):
    ans = min(ans, solve(chr(ord('a') + i)))
print(ans)