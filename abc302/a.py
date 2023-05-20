a,b = map(int, input().split())

def minimum_attacks(A, B):
    attacks_needed = (A + B - 1) // B
    return attacks_needed

minimum_attacks_needed = minimum_attacks(a, b)
print(minimum_attacks_needed)
