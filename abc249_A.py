a,b,c,d,e,f,x = map(int, input().split())
def function(a,c,x):
    person = 0
    rest = 0
    while True:
        if person + rest >= x:
            return person
        person += min(a, x - person - rest)
        rest += c

takahashi = function(a,c,x)
aoki = function(d,f,x)

if takahashi * b > aoki * e:
    print('Takahashi')
elif takahashi * b < aoki * e:
    print('Aoki')
else:
    print('Draw')