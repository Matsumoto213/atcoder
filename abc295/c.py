N = int(input())
A = list(map(int, input().split()))

def max_pairs(socks):
    sock_dict = {}
    for sock in socks:
        if sock in sock_dict:
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1
    count = 0
    for sock in sock_dict:
        count += sock_dict[sock] // 2
    return count

print(max_pairs(A))