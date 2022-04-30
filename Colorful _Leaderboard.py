N = int(input())
A = list(map(int, input().split()))
color = {'灰':0,'茶':0,'緑':0,'水':0,'青':0,'黄':0,'橙':0,'赤':0}

other = 0
for i in range(N):
    if A[i] >= 1 and A[i] <= 399:
        color['灰'] += 1
    elif A[i] < 800:
        color['茶'] += 1
    elif A[i] < 1200:
        color['緑'] += 1
    elif A[i] < 1600:
        color['水'] += 1
    elif A[i] < 2000:
        color['青'] += 1
    elif A[i] < 2400:
        color['黄'] += 1
    elif A[i] < 2800:
        color['橙'] += 1
    elif A[i] < 3200:
        color['赤'] += 1
    else:
        other += 1

mi = 0
for key,value in color.items():
    if value > 0:
        mi += 1
print(mi,mi + min(8 - mi, other))