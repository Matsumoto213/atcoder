N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def match_condition(matrix_a, matrix_b):
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            if matrix_a[i][j] == 1 and matrix_b[i][j] != 1:
                return False
    return True

def can_rotate_to_match(matrix_a, matrix_b):
    for _ in range(4):
        if match_condition(matrix_a, matrix_b):
            return True
        matrix_a = rotate_matrix(matrix_a)
    return False


if can_rotate_to_match(A, B):
    print("Yes")
else:
    print("No")