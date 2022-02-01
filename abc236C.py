a,b = map(int, input().split())
s = list(map(str, input().split()))
t = set(input().split())

for v in s:
    if v in t:
        print("Yes")
    else:
        print('No')