R,G,B,N = map(int, input().split())
cnt = 0
for r in range(N // R + 1):
    for g in range(N // G + 1):
        b = (N - (r * R + g * G)) // B
        print(b)
        if r * R + g * G + b * B == N and b >= 0:
            cnt += 1
print(cnt)