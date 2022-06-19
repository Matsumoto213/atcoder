N = int(input())
P = list(map(int, input().split()))

runner = [0] + [False] * 3
ans = 0

def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L

for i in range(len(P)):
    for j in range(i + 1):
        if P[i] == 4:
            ans += len(index_Multi(runner,True))
            ans += 1
            runner = [False] * 3

        if i == j:
            # N回目は打者がどこまで進んだかを記載する
            runner[P[i]] = True
        else:
            # それ以外はランナーがどこまで進んだかを記載する
            idx = index_Multi(runner,True)
            for k in range(len(idx)):
                if idx[k] + P[i] >= 4:
                    ans += 1
                    runner[idx[k]] = False
                else:
                    runner[idx[k] + P[i]] = True
                    runner[idx[k]] = False
            continue
        print(runner,ans)
print(ans)



