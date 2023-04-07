S = input()
import datetime
date_obj = datetime.datetime.strptime(S, '%Y/%m/%d').date()
heisei = datetime.date(2019, 4, 30)
if date_obj <= heisei:
    print('Heisei')
else:
    print('TBD')