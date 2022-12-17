S = input()
if len(S) != 8 or S[0].isdigit() or S[7].isdigit():
    print('No')
elif not S[1:7].isdecimal() or S[1] == '0':
    print('No')
else:
    print('Yes')