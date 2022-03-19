S = input()

from collections import deque
white = S.count('W')
black = S.count('B')

que = deque(S)
