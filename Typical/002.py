N = int(input())

L = ['(', ')']
def is_valid(S):
    score = 0
    for i in range(len(S)):
        if S[i] == '(':
            score += 1
        elif S[i] == ')':
            score -= 1

        if score < 0:
            return False
    
    return score == 0

from itertools import product
for pair in product(['(', ')'], repeat=N):
    if is_valid(pair):
        print(*pair, sep='')