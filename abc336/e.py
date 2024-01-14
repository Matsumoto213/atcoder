N = int(input())
def count_good_numbers(N):
    good_numbers = 0
    for i in range(1, 100):
        for j in range(10):
            num = i * 10 + j
            if num > N:
                break
            if num % i == 0:
                good_numbers += 1
    return good_numbers
# テスト
print(count_good_numbers(N))