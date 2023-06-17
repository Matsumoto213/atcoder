N = int(input())
S = input()

def duplicate_string(S):
    result = ''
    for char in S:
        result += char * 2
    return result

print(duplicate_string(S))