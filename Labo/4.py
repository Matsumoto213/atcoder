track = 0
cnt = 1
for i in reversed(range(1,801)):
    track += i
    if track >= 5000:
        cnt += 1
        track = i
print(cnt)