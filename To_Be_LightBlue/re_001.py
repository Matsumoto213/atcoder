while True:
	n,x = map(int, input().split())
	if n == x == 0:
		exit()
	ans = 0
	for i in range(1, n - 1):
	    for j in range(i + 1, n):
	        for l in range(j + 1, n + 1):
	            if i + j + l == x:
	                ans += 1
print(ans)