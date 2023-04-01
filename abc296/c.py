N,X = map(int, input().split())
A = list(map(int, input().split()))

def find_pair_with_difference(A, X):
    set_A = set(A)
    for a in set_A:
        if a + X in set_A:
            return True
    return False

if find_pair_with_difference(A, X):
    print("Yes")
else:
    print("No")