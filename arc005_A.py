n = int(input())
w = input().split()
cnt = 0
for i in range(len(w)):
    if i == len(w) - 1:
        s = w[i]
        s = s[:-1]
        w[i] = s
    if w[i] == "TAKAHASHIKUN" or w[i] == "Takahashikun" or w[i] == "takahashikun":
        cnt += 1
print(cnt)