# 問題を展開して、それを同コードで表現するのかが大事になってくる
# 問題を展開するという数学力が足りていない
# こうすれば解きやすいという感覚を覚えていくしかない

n = int(input())
ans = n

for i in range(1,10**6+1):
    if n % i == 0:
        ans = min(ans, n//i + i - 2)
print(ans)

