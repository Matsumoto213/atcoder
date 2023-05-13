N = int(input())
S = input()

def match_winner(N, S):
    takahashi_wins = 0
    aoki_wins = 0
    takahashi_first_reach = [0]* (N+1)
    aoki_first_reach = [0]* (N+1)

    for i in range(N):
        if S[i] == 'T':
            takahashi_wins += 1
            if takahashi_first_reach[takahashi_wins] == 0:
                takahashi_first_reach[takahashi_wins] = i+1
        elif S[i] == 'A':
            aoki_wins += 1
            if aoki_first_reach[aoki_wins] == 0:
                aoki_first_reach[aoki_wins] = i+1

    if takahashi_wins > aoki_wins or (takahashi_wins == aoki_wins and takahashi_first_reach[takahashi_wins] < aoki_first_reach[aoki_wins]):
        return 'T'
    else:
        return 'A'
    
print(match_winner(N,S))
