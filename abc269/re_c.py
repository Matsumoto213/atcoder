def find_subset_numbers(N):
    subset_numbers = []
    x = 0
    while x <= N:
        subset_numbers.append(x)
        x = (x - N) & N
        if x == 0:
            break
    return subset_numbers

N = int(input())
result = find_subset_numbers(N)
print(*result,sep="\n")