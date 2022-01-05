# bisectを利用しない二分探索
# これを応用してあらゆる問題に対応していく
def is_ok(mid):
    if mid > 0:
        return True
    else:
        return False
    
def binary_search(ok, ng):
    """二分探索

    Parameters
    ----------
    ok : int
    ng : int

    Returns
    -------
    ok : int
    """
    
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok