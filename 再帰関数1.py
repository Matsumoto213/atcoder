def func(n):
    if n == 0:
        return 0
    return n + func(n - 1)

def main():
    for n in range(11):
        print(n,end= "")
        print("までの和 = ", end = "")
        print(func(n))


if __name__ == '__main__':
    main()
