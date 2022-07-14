from itertools import groupby

S = input()
# RUN LENGTH ENCODING
def runLengthEncodeToString(S):
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res

print(runLengthEncodeToString(S))