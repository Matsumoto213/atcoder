N = int(input())
A = [input() for _ in range(N)]

def solve(N, A):
    ans = 0
    for i in range(N):
        for j in range(N):
            nums = []
            for k in range(N):
                nums.append(str(A[(i+k)%N][j]))
                nums.append(str(A[i][(j+k)%N]))
                nums.append(str(A[(i+k)%N][(j+k)%N]))
                nums.append(str(A[(i+k)%N][(j-k+N)%N]))
            nums = [int("".join(nums[k:k+N])) for k in range(0, len(nums), N)]
            ans = max(ans, max(nums))
    return ans


print(solve(N, A))

