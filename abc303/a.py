N = int(input())
S = input()
T = input()

def is_similar_string(S, T):
    similar_chars = {'0': 'o', 'o': '0', '1': 'l', 'l': '1'}
    
    if len(S) != len(T):
        return "No"
    
    for s, t in zip(S, T):
        if s != t and similar_chars.get(s) != t and similar_chars.get(t) != s:
            return "No"
    
    return "Yes"

print(is_similar_string(S, T))