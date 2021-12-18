N = int(input())
A = list(map(int, input().split()))
color = {'灰':0,'茶':0,'緑':0,'水':0,'青':0,'黄':0,'橙':0,'赤':0}
mi = 0
other = 0

for a in A:
    if a == 0:
        mi = mi
    elif a > 0 and a < 400:
        if color['灰'] == 0:
            mi += 1
        color['灰'] += 1
    elif a < 800:
        if color['茶'] == 0:
            mi += 1
        color['茶'] += 1
    elif a < 1200:
        if color['緑'] == 0:
            mi += 1
        color['緑'] += 1
    elif a < 1600:
        if color['水'] == 0:
            mi += 1
        color['水'] += 1
    elif a < 2000:
        if color['青'] == 0:
            mi += 1
        color['青'] += 1
    elif a < 2400:
        if color['黄'] == 0:
            mi += 1
        color['黄'] += 1
    elif a < 2800:
        if color['橙'] == 0:
            mi += 1
        color['橙'] += 1
    elif a < 3200:
        if color['赤'] == 0:
            mi += 1
        color['赤'] += 1
    else:
        other += 1
mi = max(mi,1)
print(mi, mi + other)