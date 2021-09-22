# A+B個周期なので、A+Bで割った商だけ周期を考えて、あまりをなんやかんやする
n,a,b = map(int,input().split())
 
count = (n // (a + b)) * a
# print(count)

mod = n % (a + b)
# print(mod)

if mod > a:
    count += a
else:
    count += mod
print(count)

