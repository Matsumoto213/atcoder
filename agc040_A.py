s = input()
a = [0]*(len(s) + 1)

for i in range(n):
    if s[i] == '<':
        a[i + 1] = a[i] + 1


for i in reversed(range(len(s))):
    if s[i] == '>':
        a[i] = max(a[i],a[i + 1] + 1)
        print(a)
print(sum(a))