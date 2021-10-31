S = input()
n = len(S)
black = 0
total = 0
for i in range(n):
  if S[i] == 'W':
    total += black
  elif S[i] == 'B':
    black += 1
 
print(total)