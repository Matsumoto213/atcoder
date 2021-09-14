s = input()
t = input()

if s == t:
    print("Yes")

count = 0
while True:
    if count == len(s):
        break
    s = s[-1]+s[:len(s) - 1]

    if s == t:
        print("Yes")
        exit(0)
    count += 1
print("No")
    