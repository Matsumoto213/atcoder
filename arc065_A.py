def judge():
    S = input()[::-1]
    T = ['dream','dreamer','erase','eraser']
    t = [str(s)[::-1] for s in T]
    
    ans = ""
    idx = 0
    while True:
        if idx >= len(S):
            break    
        for j in range(idx + 1,len(S) + 1):
            temp = S[idx:j + 1]
            if temp in t:
                ans = temp[::-1] + ans
                idx += len(ans)
        else:
            idx += 1
        if len(ans) == len(S):
            return True
        return False
            
print('YES' if judge() else 'NO')
