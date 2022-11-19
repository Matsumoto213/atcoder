H,M = input().split()

if len(H) == 1:
    H = '0' + H

if len(M) == 1:
    M = '0' + M 

while True:
    H = [int(H[i]) for i in range(2)]
    M = [int(M[i]) for i in range(2)]
    temp = M[0]
    M[0] = H[1]
    H[1] = temp

    H = [str(H[i]) for i in range(2)]
    M = [str(M[i]) for i in range(2)]
    H = ''.join(H)
    M = ''.join(M)
    H = int(H)
    M = int(M)
    if 0 <= H <= 23 and 0 <= M <= 59:
        H = str(H)
        M = str(M)
        if len(H) == 1:
            H = '0' + H
        if len(M) == 1:
            M = '0' + M
        H = [H[i] for i in range(2)]
        M = [M[i] for i in range(2)]
        temp = M[0]
        M[0] = H[1]
        H[1] = temp
        H = [int(H[i]) for i in range(2)]
        M = [int(M[i]) for i in range(2)]
        H = [str(H[i]) for i in range(2)]
        M = [str(M[i]) for i in range(2)]
        H = ''.join(H)
        M = ''.join(M)
        H = int(H)
        M = int(M)
        print(H,M)
        exit()
    H = str(H)
    M = str(M)
    if len(H) == 1:
        H = '0' + H
    if len(M) == 1:
        M = '0' + M
    H = [H[i] for i in range(2)]
    M = [M[i] for i in range(2)]
    temp = M[0]
    M[0] = H[1]
    H[1] = temp
    H = ''.join(H)
    M = ''.join(M)
    H = int(H)
    M = int(M)
    if M < 60:
        M += 1
    # 60分になったら
    if M == 60:
        # 24時は存在しないためなし
        if H < 24:
            H += 1
        else:
            H = 0
        M = 0
    H = str(H)
    M = str(M)
    if len(H) == 1:
        H = '0' + H
    if len(M) == 1:
        M = '0' + M
    H = [H[i] for i in range(2)]
    M = [M[i] for i in range(2)]