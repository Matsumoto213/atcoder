S = input()
T = input()

def can_win(S, T):
    replaceable = 'atcoder'
    S_counts = {char: S.count(char) for char in replaceable}
    T_counts = {char: T.count(char) for char in replaceable}
    S_counts['@'] = S.count('@')
    T_counts['@'] = T.count('@')
    for char in replaceable:
        if S_counts[char] < T_counts[char]:
            needed = T_counts[char] - S_counts[char]
            if S_counts['@'] >= needed:
                S_counts['@'] -= needed
            else:
                return 'No'
        elif T_counts[char] < S_counts[char]:
            needed = S_counts[char] - T_counts[char]
            if T_counts['@'] >= needed:
                T_counts['@'] -= needed
            else:
                return 'No'
    return 'Yes' if S_counts['@'] == T_counts['@'] else 'No'

print(can_win(S,T))