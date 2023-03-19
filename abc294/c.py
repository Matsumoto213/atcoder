import bisect

def find_positions(A, B):
    C = sorted(A + B)

    positions_A = [bisect.bisect_left(C, a) + 1 for a in A]
    positions_B = [bisect.bisect_left(C, b) + 1 for b in B]

    return positions_A, positions_B


# 長さNの狭義単調増加列Aと長さMの狭義単調増加列Bの例
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

positions_A, positions_B = find_positions(A, B)
print(*positions_A)
print(*positions_B)