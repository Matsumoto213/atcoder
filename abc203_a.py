a,b,c = map(int, input().split())

if a != b and a != c and b != c:
    print("0")
elif a == b and b == c and a == c:
    print(a)
else:
    if a == b and a != c:
        print(c)
    elif a == c and a != b:
        print(b)
    else:
        print(a)
