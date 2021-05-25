class Questions(object):

    """
    A string is valid if it is sorted, the string must only contain
    A or/and B, e.g., 'AAAA', 'AABB', 'BB' are valid strings. while
    'BBAA' is not a valid string.

    Given a string only contains 'A' or 'B', compute the minimun
    number of characters need to be deleted to make a valid string.

    e.g., 'BBAAAA' should return 2 to make 'AAAA'
    e.g., 'BAABBBAB' should return 2 to make 'AABBB'
    """
    @classmethod
    def del_to_ABstr(cls, S):
        if len(S) <= 1:
            return 0

        cnt_a, cnt_b = S.count('A'), S.count('B')
        if cnt_b == 0 or cnt_a == 0:
            return 0

        inda = S.index('A')
        rindb = S.rindex('B')
        if rindb < inda: ### for cases 'BBAAAA' we can return min num of 'A' and 'B'
            return min([cnt_a, cnt_b])
        
        ## a invalid case 'BAAABAAB' can be deduced to be 'AAABAAB',
        ## so the begin and end is valid, then we can recursively check the middle of the str.
        valid_beg_end = S[inda:rindb+1]
        delAB = len(S) - len(valid_beg_end)
        
        indb, rinda = valid_beg_end.index('B'), valid_beg_end.rindex('A')
        if rinda > indb: ### otherwise already a valid string, delete nothing more!
            invalid_s = valid_beg_end[indb:rinda+1]
            delAB += cls.del_to_ABstr(invalid_s)
        return min([delAB, cnt_a, cnt_b])

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

            



