S = input()
reverse = S[::-1]
for _ in range(10 ** 4):
    if S == reverse:
        print('Yes')
        exit()
    S = 'a' + S
    reverse = reverse + 'a'
print('No')