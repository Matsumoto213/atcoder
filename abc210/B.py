n = int(input())
S = input()

for i in range(len(S)):
    # 高橋の番
    if i % 2 == 0 and S[i] == '1':
        print('Takahashi')
        break
    elif i % 2 != 0 and S[i] == '1':
        print('Aoki')
        break