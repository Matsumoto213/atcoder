N,T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

def find_winner(N, C, R, T):
    color_t = C[0]
    t_present = False
    max_value_same_color_as_t = -1
    winner_same_color_as_t = -1

    max_value_color_t = -1
    winner_color_t = -1

    for i in range(N):
        color, value = C[i], R[i]

        if color == color_t:
            if value > max_value_same_color_as_t:
                max_value_same_color_as_t = value
                winner_same_color_as_t = i + 1

        if color == T:
            t_present = True
            if value > max_value_color_t:
                max_value_color_t = value
                winner_color_t = i + 1

    if t_present:
        return winner_color_t
    else:
        return winner_same_color_as_t

winner = find_winner(N, C, R, T)
print(winner)
