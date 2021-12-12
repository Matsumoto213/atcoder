# 最後に出力する際に大きな数になる可能性があるためあまりを出力しなさい
# この場合には数が大きくなるとTLEになる可能性があるので、forループで繰り返すたびに余りを行うと計算量が小さくなることがある

N = int(input())

mod = 10 ** 9 + 7
ans = 1
for i in range(N):
    i += 1
    
    ans *= i
    ans %= mod
print(ans)