a,b = map(int, input().split())
temp = round(b / a,3)
if len(str(temp)) == 3:
    print(str(temp) + '00')
else:
    print(temp)