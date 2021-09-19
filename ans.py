def main():
    X = input()
    D = dict()
    for i in range(26):
        nxt = chr(i + ord('a'))  # 英小文字の前から数えてi番目（aを0番目とする）は、これで生成できます
        D[X[i]] = nxt
    print(D)
 
    N = int(input())
    A = []
    for _ in range(N):
        S = input()
        T = ''
        for char in S:
    
            T += D[char]
        A.append((T, S))
    A.sort()  # タプルをソートすると、まず1要素目の変換後の名前の順で並び替えます  # 変換後の名前が同じなら、2要素目の名前の順でソートされますが、今回は同じ名前はありません
    print(A)
    for i in range(N):
        print(A[i][1])  # 変換前の名前です
 
 
if __name__ == '__main__':
    main()
