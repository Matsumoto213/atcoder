S = input()
N = len(S)
count = 0

i = 0
while True:
    if i == len(S) - 1:
        break
    string = S[i:i + 2]
    if string == "10" or string == "01":
        S = S[:i]+S[i + 2:]
        count += 2
        i -= 1
    else:
        i += 1
print(count)