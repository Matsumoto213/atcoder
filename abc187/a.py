a,b = map(int, input().split())
def sum_digit(num):
    hundreds_digit = num // 100
    tens_digit = (num // 10) % 10
    ones_digit = num % 10
    return hundreds_digit + tens_digit + ones_digit

print(max(sum_digit(a),sum_digit(b)))