A,B,W = map(int, input().split())

def calculate_min_max_mikan(A, B, W):
    W = W * 1000

    min_mikan = (W + B - 1) // B
    max_mikan = W // A
    
    if min_mikan > max_mikan:
        print("UNSATISFIABLE")
    else:
        print(min_mikan, max_mikan)

calculate_min_max_mikan(A, B, W)