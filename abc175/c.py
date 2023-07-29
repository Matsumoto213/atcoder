def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    q, r = divmod(X, D)

    if K < q:
        print(X - K * D)
    else:
        print(D - r if (K - q) % 2 else r)

main()