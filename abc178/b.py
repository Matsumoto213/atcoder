N = int(input())

conti_judge = 0
for _ in range(N):
    a,b = map(int, input().split())
    if a == b:
        conti_judge += 1
    else:
        conti_judge = 0
    
    if conti_judge == 3:
        print('Yes')
        exit()

print('No')