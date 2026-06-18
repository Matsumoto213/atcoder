ans = 0

for i in range(1,1000):
    for j in range(i + 1, 1000):
        for k in range(j + 1, 1000):
            goukei = i * j // 2
            if goukei <= 6000:
                if i ** 2 + j ** 2 == k ** 2:
                    print(i,j,k, goukei)
                    ans +=1
            else:
                continue

print(ans)