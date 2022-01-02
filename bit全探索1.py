money = 300
item = (('みかん',100),('りんご',200),('ぶどう',300))
n = len(item)

for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(item[j][0])
    print(bag)