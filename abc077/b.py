N = int(input())
  
for i in range(N,0,-1):
    # Nからひとつずつ見ていって何かの数の平方根であればそれを出力してストップ
    if (i ** .5).is_integer():
        print(i)
        exit(0)