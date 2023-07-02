from fractions import Fraction
N = int(input())

ansList = []
for i in range(N):
    a,b = map(int, input().split())
    ans = Fraction(a, a+b)
    ansList.append([ans,i + 1])

array = sorted(ansList, key=lambda x: x[0],reverse=True)

ans = [x[1] for x in array]
print(*ans)