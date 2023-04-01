import random

def find_minimum_x(N, M):
    for a in range(1, N + 1):
        b = -(-M // a)
        if b <= N and a * b >= M:
            return a * b
    return -1

def generate_test_case():
    N = random.randint(1, 10**12)
    M = random.randint(1, 10**12)
    return N, M

for i in range(20):
    N, M = generate_test_case()
    print(f"Test case {i+1}: N={N}, M={M}")
    result = find_minimum_x(N, M)
    print("X:", result)
