N = int(input())
S = input()

for i in range(len(S)):
    temp = ord(S[i]) + N
    if temp > 90:
        temp -= 26
    print(chr(temp),end = "")
print()