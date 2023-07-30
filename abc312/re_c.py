N,M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def min_price(A, B):
    A.sort()
    B.sort()
    print(A)
    print(B)
    left = 0
    right = max(max(A), max(B)) + 1

    while right - left > 1:
        mid = (left + right) // 2
        count_A = 0
        for s in A:
            if s <= mid:
                count_A += 1
        count_B = 0
        for b in B:
            if b >= mid:
                count_B += 1
        if count_A >= count_B:
            right = mid
        else:
            left = mid
        print(left, right, count_A,count_B)
    return right

print(min_price(A, B))