from questions.str_related import Questions

def test_del_str_costs(func=Questions.del_str_costs):
    assert 0 == func('ababc', [0,1,2,3,4])
    assert 4 == func('abbbc', [0,1,5,3,4])
    assert 4 == func('accbb', [1,2,3,2,3])
    assert 21 == func('abccccddccc', [0,0,1,2,7,3,5,8,1,9,20])
    assert 3 == func('aaaaa', [0,0,1,2,7])
    assert 0 == func('', [])

def test_del_to_ABstr(func=Questions.del_to_ABstr):
    assert 2 == func('BBAAAA')
    assert 2 == func('BAABBBAB')
    assert 0 == func('AABBBBBBBB')
    assert 0 == func('')
    assert 3 == func('ABABAAABBBA')
    assert 1 == func('AABAB')
    assert 3 == func('ABABABAB')
    assert 2 == func('BAAABAAB')
    
