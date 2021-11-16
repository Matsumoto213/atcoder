# どうすれば二重ループを使わないで行うことができるかどうかがこの問題の焦点
ans = 0
def solution(lst):
    for i in lst:
        ans += n ** n
    return (ans - sum(a) ** 2)

N = int(input())
A = list(map(int, input().split()))
print(solution(A))
        
