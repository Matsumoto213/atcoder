S = input()
while True:
    S = S[:-1]
    lenS = len(S)
    
    if lenS % 2 == 0:
        half = lenS // 2
        left = S[:half]
        right = S[half:]
        
        if left == right:
            print(len(S))
            exit(0)