a,b,c,d,e = map(int, input().split())
from collections import Counter

def judgeFullHouse(a,b,c,d,e):
    l = [a,b,c,d,e]
    L = Counter(l)
    two = 0
    three = 0
    for value in L.values():
        if value == 2:
            two += 1
        elif value == 3:
            three += 1
    
    if len(L) == 2 and two == 1 and three == 1:
        return True

    return False

print('Yes' if judgeFullHouse(a,b,c,d,e) else 'No')