N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
import itertools

judge = True
for i in range(N - 2):
    temp1 = abs(A[i] - A[i + 1])
    temp2 = abs(A[i] - B[i])
    temp3 = abs(B[i] - A[i + 1])
    temp4 = abs(B[i] - B[i + 1])
    temp5 = abs(A[i] - A[i + 2])
    temp6 = abs(A[i] - B[i + 2])
    temp7 = abs(B[i] - A[i + 2])
    temp8 = abs(B[i] - B[i + 2])
    print(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8)
    if (temp1 > K and temp2 > K and temp3 > K and temp4 > K) or (temp5 > K * 2 and temp6 > K * 2 and temp7 > K * 2 and temp8 > K * 2):
        judge = False

print('Yes' if judge else 'No')