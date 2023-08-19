N = int(input())
ice_creams = []
for _ in range(N):
    F, S = map(int, input().split())
    ice_creams.append((S, F))

# 美味しさで降順にソート
ice_creams.sort(reverse=True)

# 最も美味しいアイスクリーム
max_satisfaction = ice_creams[0][0]

# 同じ味で2番目に美味しいアイスクリームを探す
second_same_flavor_satisfaction = 0
for i in range(1, N):
    if ice_creams[i][1] == ice_creams[0][1]:
        second_same_flavor_satisfaction = ice_creams[i][0]
        break

# 最も美味しいアイスクリームと異なる味の中で最も美味しいものを探す
max_different_flavor_satisfaction = 0
for i in range(1, N):
    if ice_creams[i][1] != ice_creams[0][1]:
        max_different_flavor_satisfaction = ice_creams[i][0]
        break

answer = max_satisfaction + max(max_different_flavor_satisfaction, second_same_flavor_satisfaction / 2)
print(int(answer))
