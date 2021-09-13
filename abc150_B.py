n = int(input())
s = input()

count = 0

for i in range(n - 2):
    ans = s[i:i + 3]
    if ans = "ABC":
        count += 1
print(count)


# もっと効率の良い方法
N = int(input())
S = input()
print(S.count('ABC'))