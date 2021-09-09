# 自分の提出コード
n,x = map(int, input().split())

a = 0
over = 0
for i in range(n):
    # 飲んだお酒の量はv,アルコール度数はp
    v,p = map(int, input().split())
    a += p * v

    if ans > x * 100:
        print(i + 1)
        over = 1
        break
 
if over == 0:
    print(-1)


    


