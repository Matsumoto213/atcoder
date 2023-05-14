def solve(N):
    count = 0
    for A in range(1, N):
        for B in range(1, N):
            if A * B > N:  # 早期にループを抜けるための条件
                break
            for C in range(1, N):
                D = N - A * B
                if D < 0:  # 早期にループを抜けるための条件
                    break
                if D % C == 0 and D / C == C:  # 積の和がNと等しいか確認
                    count += 1
    return count


N = int(input())
print(solve(N))
