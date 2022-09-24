a,b = map(int, input().split())

takahashi = [False,False,False]
Aoki = [False,False,False]


if a == 1:
    takahashi[0] = True
elif a == 2:
    takahashi[1] = True
elif a == 4:
    takahashi[2] = True
elif a == 3:
    takahashi[0] = True
    takahashi[1] = True
elif a == 5:
    takahashi[0] = True
    takahashi[2] = True
elif a == 6:
    takahashi[1] = True
    takahashi[2] = True
elif a == 7:
    takahashi[0] = True
    takahashi[1] = True
    takahashi[2] = True


if b == 1:
    Aoki[0] = True
elif b == 2:
    Aoki[1] = True
elif b == 4:
    Aoki[2] = True
elif b == 3:
    Aoki[0] = True
    Aoki[1] = True
elif b == 5:
    Aoki[0] = True
    Aoki[2] = True
elif b == 6:
    Aoki[1] = True
    Aoki[2] = True
elif b == 7:
    Aoki[0] = True
    Aoki[1] = True
    Aoki[2] = True

ans = 0
for i in range(3):
    if i == 0:
        if takahashi[i] or Aoki[i]:
            ans += 1
    elif i == 1:
        if takahashi[i] or Aoki[i]:
            ans += 2
    else:
        if takahashi[i] or Aoki[i]:
            ans += 4
print(ans)
