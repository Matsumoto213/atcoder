N = int(input())
S = input()

def check_star_between_pipes(S):
    star_index = S.find('*')
    pipe1_index = S.find('|')
    pipe2_index = S.rfind('|')
    
    if pipe1_index < star_index < pipe2_index:
        return 'in'
    else:
        return 'out'
    
result = check_star_between_pipes(S)
print(result)