s = input()
n = len(s)
ans = 10 ** 11 + 7

def solve(C):
    count = 0
    t = s
    while True:
        if len(set(t)) == 1:
            return count
        
        # 空のリストを用意してループが終了するたびにtをmのリストに入れ替える
        m = []
        for i in range(len(t) - 1):
            if t[i] == C or t[i + 1] == C:
                m.append(C)
            else:
                m.append(t[i])
        t = "".join(m)
        count += 1
        

for i in range(26):
    ans = min(ans, solve(chr(ord('a') + i)))
print(ans)