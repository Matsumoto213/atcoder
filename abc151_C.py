n,m = map(int, input().split())
ac = []
wa = []

for i in range(m):
    problem,judge = input().split()
    problem = int(problem)
    if problem == n and judge == "AC":
        ac.append(problem)
        break
    
    if judge == "WA":
        wa.append(problem)
    else:
        ac.append(problem)
print(len(set(ac)),len(set(wa)))