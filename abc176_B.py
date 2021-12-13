N = input()
N = [int(N[i]) for i in range(len(N))]
sumN = sum(N)

print("Yes" if sumN % 9 == 0  else "No")