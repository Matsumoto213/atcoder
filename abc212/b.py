pas = input()
len_ = len(set(pas))

if len_ == 1:
    print("Weak")
    exit()

for i in range(len(pas) - 1):
    now = int(pas[i])
    next = int(pas[i + 1])

    if now == 9:
        if next != 0:
            print("Strong")
            exit()
    else:
        if now + 1 != next:
            print("Strong")
            exit()
print("Weak")