# なぜかエラーになってしまう
N = int(input())
A = list(map(int, input().split()))
rate = {'hai':0,'tya':0,'midori':0,',mizu':0,'ao':0,'ki':0,'syu':0,'aka':0}
other = 0
mi = 0
for a in A:
    if a == 0:
        mi = mi
    elif a > 0 and a < 400:
        if rate['hai'] == 0:
            mi += 1
        rate['hai'] += 1
    elif a >= 400 and a < 800:
        if rate['tya'] == 0:
            mi += 1
        rate['tya'] += 1
    elif a >= 800 and a < 1200:
        if rate['midori'] == 0:
            mi += 1
        rate['midori'] += 1
    elif a >= 1200 and a < 1600:
        if rate['mizu'] == 0:
            mi += 1
        rate['mizu'] += 1
    elif a >= 1600 and a < 2000:
        if rate['ao'] == 0:
            mi += 1
        rate['ao'] += 1
    
    elif a >= 2000 and a < 2400:
        if rate['ki'] == 0:
            mi += 1
        rate['ki'] += 1
    elif a >= 2400 and a < 2800:
        if rate['syu'] == 0:
            mi += 1
        rate['syu'] += 1
    elif a >= 2800 and a < 3200:
        if rate['aka'] == 0:
            mi += 1
        rate['aka'] += 1
    else:
        other += 1
print(mi, mi + other)