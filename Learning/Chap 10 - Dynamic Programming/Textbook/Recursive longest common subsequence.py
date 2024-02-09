"""

"""


def reclcs(X, Y):
    if X == "" or Y == "":
        return ""
    if X[-1] == Y[-1]:
        return reclcs(X[:-1], Y[:-1]) + X[-1]
    else:
        return max([reclcs(X[:-1], Y), reclcs(X, Y[:-1])], key=len)


"""
def lcs(X, Y):
    t = {}
    for i in range(len(X)+1): t[(i,0)] = ""
    for j in range(len(Y)+1): t[(0,j)] = ""
    
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                t[(i+1,j+1)] = t[(i, j)] + x
            else:
                t[(i+1,j+1)] = max([t[(i, j+1)], t[(i+1, j)]], key = len)
    return t[(len(X), len(Y))]
"""
