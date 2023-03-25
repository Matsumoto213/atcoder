N,M,K = map(int, input().split())
A = list(map(int, input().split()))

def expected_AK(N, M, K, A):
    MOD = 998244353

    # 操作1: 0の要素を1からMまでの整数で置き換える
    zero_count = A.count(0)
    expected_values = [(i + 1) / M for i in range(M)]

    # 0の要素を期待値に置き換える
    A = [value if value != 0 else expected_values for value in A]
    A = [item for sublist in A for item in (sublist if isinstance(sublist, list) else [sublist])]

    # 操作2: Aを昇順に並び替える
    A.sort()

    # A_Kの期待値を計算
    expected_AK = sum(A[K - 1 - i] * (zero_count - i) / (i + 1) for i in range(zero_count + 1)) % MOD

    return int(expected_AK)
result = expected_AK(N, M, K, A)
print(result)