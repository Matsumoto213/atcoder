s = input()
n = int(input())
for i in range(n):
    l,r = map(int, input().split())
    ans = s[l - 1:r]
    ans = ans
    result = [ans[i] for i in range(len(ans))]
    result = result[::-1]
    ans = "".join(result)
    s = s[:l - 1]+ans+s[r:]
print(s)