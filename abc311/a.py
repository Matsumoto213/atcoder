N = int(input())
S = input()

def find_first_occurrences(S):
    counts = {'A': 0, 'B': 0, 'C': 0}
    for i, char in enumerate(S, 1):
        if char in counts:
            counts[char] += 1
            if all(value >= 1 for value in counts.values()):
                return i
    return -1
print(find_first_occurrences(S))