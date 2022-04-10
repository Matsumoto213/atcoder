N,A,B = map(int, input().split())

if (A + B) % 2 == 0:
    print(B - (A + B) // 2)
else:
    temp_min = min(A - 1, N - B)
    print(temp_min + 1 + ((B - A - 1) // 2))