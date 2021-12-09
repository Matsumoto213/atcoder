N = int(input())
ans = str((1.8 * N) + 32)

if ans[-1] == '0':
    ans = int(ans)

print(ans)