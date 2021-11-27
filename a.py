s = input()
t = input()

if s[0] == "#" and s[1] == "#" and t[0] == "#" and t[1] == "#":
    print("Yes")
elif s[0] == "#" and s[1] == "#" and t[1] == "#" and t[0] == ".":
    print("Yes")
elif s[0] == "#" and s[1] == "#" and t[0] == "#" and t[1] == ".":
    print("Yes")
elif s[0] == "#" and t[0] == "#" and t[1] == "#" and s[1] == ".":
    print("Yes")
elif s[1] == "#" and t[0] == "#" and t[1] == "#" and s[0] == ".":
    print("Yes")
elif s[0] == "#" and t[0] == "#" and s[1] == "." and t[1] == ".":
    print("Yes")
elif s[1] == "#" and t[1] == "#" and s[0] == "." and t[0] == ".":
    print("Yes")
elif s[0] == "#" and s[1] == "#" and t[0] == "." and t[1] == ".":
    print("Yes")
elif t[0] == "#" and t[1] == "#" and s[0] == "." and s[1] == ".":
    print("Yes")
else:
    print("No")
    