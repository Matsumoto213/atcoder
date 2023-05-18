N = int(input())
A = list(map(int, input().split()))

def calc_sum_of_squared_diffs(A):
    N = len(A)
    sum_A = sum(A)
    sum_A_squared = sum(x ** 2 for x in A)
    return N * sum_A_squared - sum_A ** 2

ans = calc_sum_of_squared_diffs(A)
print(ans)