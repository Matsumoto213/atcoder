x1,y1,x2,y2 = map(int,input().split())

diff_x = x2 - x1
diff_y = y2 - y1

y3 = diff_x + y2
x3 = x2 - diff_y 

x4 = x3 - diff_x
y4 = y3 - diff_y

print(x3, y3, x4, y4)
