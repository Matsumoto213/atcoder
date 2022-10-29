from functools import lru_cache
@lru_cache

# キャッシュをクリアして高速化する
# ２度同じ計算をすることなく、returnするため高速化を実現することができる。
# その際returnする値が//で割り切らなければ再起することができずにエラーが起きてしまう。

def function(n):
    if n == 0:
        return 1
    
    return function(n // 2) + function(n // 3)
N = int(input())
print(function(N))