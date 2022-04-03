x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

import collections
x = [x1,x2,x3]
y = [y1,y2,y3]

X = collections.Counter(x)
Y = collections.Counter(y)


for key,value in X.items():
    if value == 1:
        ansx = key

for key,value in Y.items():
    if value == 1:
        ansy = key

print(ansx,ansy)