N = int(input())
boxes = [list(map(int, input().split())) for _ in range(N)]

def is_adjacent(box1, box2):
    touch = 0
    overlap = 0
    for d in range(3):
        b1_min, b1_max = sorted([box1[d], box1[d+3]])
        b2_min, b2_max = sorted([box2[d], box2[d+3]])
        if (b1_min == b2_max) or (b1_max == b2_min):
            touch += 1
        elif not (b1_max < b2_min or b2_max < b1_min):
            overlap += 1
    return overlap == 2 and touch == 1

ans = [0]*N
for i in range(N):
    for j in range(i+1, N):
        if is_adjacent(boxes[i], boxes[j]):
            ans[i] += 1
            ans[j] += 1

for a in ans:
    print(a)
