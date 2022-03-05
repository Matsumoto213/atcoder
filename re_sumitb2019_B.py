N = int(input())
i = 1

while True:
    temp = int(i * 1.08)
    if  temp > N:
        break

    if temp == N:
        print(i)
        exit()
    
    i += 1

print(':(')