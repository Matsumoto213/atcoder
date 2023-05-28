N,M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]

def find_unfriendly_pairs(N, M, photos):
    adjacent = [[0]*N for _ in range(N)]
    for photo in photos:
        for j in range(N-1):
            smaller = min(photo[j], photo[j+1]) - 1
            larger = max(photo[j], photo[j+1]) - 1
            adjacent[smaller][larger] = 1
    unfriendly_pairs = 0
    print(adjacent)
    for i in range(N):
        for j in range(i+1, N):
            print(adjacent[i][j],i,j)
            if not adjacent[i][j]:
                unfriendly_pairs += 1
    return unfriendly_pairs

print(find_unfriendly_pairs(N, M, a))