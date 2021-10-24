# 再帰関数でやってみる
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 再帰呼び出し
    return fibo(n - 1) + fibo(n - 2)

def main():
    for i in range(10):
        print(str(i)+"項目の値: " + str(fibo(i)))

if __name__ == '__main__':
    main()