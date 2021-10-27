from itertools import product

abcd = input()

def solve():
    S = 0
    for i in range(3):
        if pro[i]:
            abcd = abcd[i:i+1]+"+"+abcd[i:]
        else:
            abcd = abcd[i:i+1]+"-"+abcd[i:]
        

        if ans == 7:
            return abcd


digits = len(abcd)

for pro in product((0, 1), repeat=3):
    ans = solve(pro)+"= 7"

print(ans)