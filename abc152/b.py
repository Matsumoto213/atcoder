a,b = input().split()
ans = []
ans.append(a * int(b))
ans.append(b * int(a))

ans.sort()
print(ans[0])