class Questions(object):
    """
    Given a string S, and an cost array C,
    if the adjacent charactor is exactly the same, delete it with the min cost.

    the size of S and C are totally the same.

    e.g., S='ababc', C=[0,1,2,3,4], return 0
    e.g., S='abbbc', C=[0,1,5,3,4], return 4, because 3'b's has cost 1,5,3, and
            minimun sum of the costs should be 1 + 3 that we would like to delete
    e.g., S='accbb' C=[1,2,3,2,3], return 4, because we need to delete 'c' and 
            'b', while the min cost of 'c' is 2, and the min cost of 'b' is 2 too.        
    """
    @classmethod
    def del_str_costs(cls, S, C):
        if S=='':
            return 0
        
        cur = S[0]
        lsls = []
        tmpls = []
        for id, ch in enumerate(S):
            if ch == cur:
                tmpls.append(C[id])
            else:
                cur = ch
                lsls.append(tmpls)
                tmpls = [C[id]]
        lsls.append(tmpls)
        res = 0
        for ls in lsls:
            if len(ls) > 1:
                res += sum(ls) - max(ls)
        return res

            



