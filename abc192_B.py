def judge():
    S = input()
    
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i].isupper():
                return False
        else:
            if S[i].islower():
                return False
    # 全てをくぐり抜ければTrue
    return True
        
        
print("Yes" if judge() else "No")