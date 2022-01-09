N = int(input())
h = list(map(int, input().split()))

l = [0] * N

t = 0
i = 0

judge_s = False
judge_f = False

start = 0
finish = N - 1

while True:
    if l == h:
        print(t)
        break
        
    # スタート位置を決める
    if judge_s == False and h[i] > l[i]:
        judge_s = True
        start = i
    
    # スタート位置が決まっていて、かつh[i]と比べて足りている場合はfinishを決める
    if judge_s == True and h[i] == l[i]:
        judge_f = True
        finish = i

    if i == N - 1 and judge_s == True and judge_f == False:
        judge_f = True
        finish = i + 1

    i += 1
    # どっちも定まったタイミングでループ処理を開始する
    if judge_s == judge_f == True:
        for i in range(start,finish):
            l[i] += 1
        judge_s = False
        judge_f = False
        i = 0
        t += 1
        