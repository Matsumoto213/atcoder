N = int(input())
price = [100,101,102,103,104,105]
def judge(n):
    for i in range(5):
        temp = 0
        tem = price[i]
        
        if n % temp == 0:
            return True
            
        for j in range(i + 1,len(price)):
            temp = price[i] + price[j]  
            tem += price[j]
            print(temp,tem)
            if n % temp == 0 or tem % n == 0:
                return True
    return False

print(1 if judge(N) else 0)