import bisect
li = [2, 5, 8, 13, 13, 18, 25, 30]

# bisect_leftとbisect_rightの違いは同じ値があったときに一番左に入れるのか一番右に入れるのかだけの違い
ind = bisect.bisect_right(li, 28)

# insort_leftとinsert_rightも上の説明と同様
bisect.insort_right(li, 13)