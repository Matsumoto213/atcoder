S = list(map(int, input().split()))

def judge(S):
    for i in range(len(S)):
        if i != len(S) - 1:
            if S[i] > S[i + 1]:
                return False

        if S[i] < 100 or S[i] > 675:
            return False
        
        if S[i] % 25 != 0:
            return False
    return True

print('Yes' if judge(S) else 'No')