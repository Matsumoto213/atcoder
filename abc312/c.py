N,M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def min_price(N, M, sellers, buyers):
    sellers.sort()
    buyers.sort()

    left = 0
    right = max(max(sellers), max(buyers)) + 1

    while right - left > 1:
        mid = (left + right) // 2
        if sum(1 for s in sellers if s <= mid) >= sum(1 for b in buyers if b >= mid):
            right = mid
        else:
            left = mid

    return right

print(min_price(N, M, A, B))