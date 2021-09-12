a,b = map(int, input().split())
c,d = map(int, input().split())

a_b = max(a,b)
c_d = min(c,d)

print(a_b - c_d)