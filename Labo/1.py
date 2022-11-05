fibo = [0] * 50
fibo[0] = 1
fibo[1] = 0
fibo[2] = 5

for i in range(3,50):
    fibo[i] = fibo[i - 3] + fibo[i - 1]

print(fibo)