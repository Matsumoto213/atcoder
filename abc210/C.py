from collections import Counter

n,k = map(int, input().split())
C = list(map(int, input().split()))

counter = Counter(C[:k])
# cnt = Counter(C)

len_counter = len(counter)
# print(counter,cnt)
# リストの中で連続する整数が異なっているかその最大の種類数を数える。

for i in range(k,n):
    left = C[i - k]
    right = C[i]
    counter[left] -= 1
    counter[right] += 1
    if counter[left] == 0:
        del counter[left]
    len_counter = max(len_counter, len(counter))

print(len_counter)