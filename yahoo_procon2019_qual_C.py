K,A,B = map(int,input().split())

bis = 1
money = 0

# A円貯めるまでとビスケットを1枚叩いて増やした方がいいのかを判断する
for _ in range(K):
    if money != 1:
        
        # 交換までのビスケットの枚数に足りていない場合(B)
        if bis < A:
            bis += 1

        # 足りている場合はa関数を用いて交換する
        else:
            bis = 0
            money = 1
    
    else:
        money = 0
        bis = B
        
    print(bis,money)
        
print(bis)
        
        
        
    
    