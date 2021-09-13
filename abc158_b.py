n,a,b = map(int, input().split())

ans = ''
while True:
    if len(ans) >= n:
        break
    ans = ans+'b'*a
    ans = ans+'r'*b

result = ans[:n]

print(result.count('b'))

