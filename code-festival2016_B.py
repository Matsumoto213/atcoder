n,a,b = map(int, input().split())
s = input()


passing = 0
b_count = 0
for i in range(len(s)):
    if s[i] == "a" and passing < a + b:
        passing += 1
        print("Yes")
    elif s[i] == "b":
        b_count += 1
        if passing < a + b and b_count <= b:
            passing += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")

