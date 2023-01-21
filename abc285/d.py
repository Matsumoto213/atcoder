class UnionFind:
    def __init__(self,N):
        self.N=N
        self.parent_size=[-1]*N
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
    def same(self,a,b):
        return self.leader(a) == self.leader(b)

# 入力の受け取り
N=int(input())

# UnionFindを用意
UF=UnionFind(2*N+2)

# 連想配列(defaultdict)を用意
from collections import defaultdict

# 名前→頂点番号への変換用連想配列
# 初期値は0
Num=defaultdict(int)


for i in range(1,N+1):
    # 入力の受け取り
    S,T=map(str, input().split())
    # Sに番号がまだ振られていなければ
    if Num[S]==0:
        # 2i番を振る
        Num[S]=2*i
    # Sに番号がまだ振られていなければ
    if Num[T]==0:
        # (2i+1)番を振る
        Num[T]=2*i+1
    
    # SとTが連結であれば
    if UF.same(Num[S],Num[T]):
        # ループになるので「No」
        print("No")
        # 終了
        exit()
    # そうでなければ
    else:
        # 連結にする⇔辺を張る
        UF.merge(Num[S],Num[T])
print("Yes")