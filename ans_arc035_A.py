# ものごっついわかりやすいコード
S = input()
f = True

for i, j in zip(s, reversed(s)):
    if i == "*" or j == "*":
        continue
    
    if i != j:
        f = False
        
print("YES" if f == True else "NO")