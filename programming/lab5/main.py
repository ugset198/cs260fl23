from lab5 import *


if __name__ == '__main__':
    test = '1'
    num = '0111' # 7
    expected_ans = '1001' # -7 
    print('testing two complement: {0} --> {1}', num, expected_ans)
    res = twos_complement(num)
    message = "Test# {0}: on {1} expected {2}, got: {3}".format(test,num,expected_ans,res)
    assert expected_ans == res, message
    print('ok')


    test = '2'
    num = '0110' # 6
    expected_ans = '1010' # -6 
    print('testing two complement: {0} --> {1}', num, expected_ans)
    res = twos_complement(num)
    message = "Test# {0}: on {1} expected {2}, got: {3}".format(test,num,expected_ans,res)
    assert expected_ans == res, message
    print('ok')

    '''
    write more test cases

    test = ''
    num = '01000' # 8
    expected_ans = '11000' # -8 
    print('testing two complement: {0} --> {1}', num, expected_ans)
    res = twos_complement(num)
    message = "Test# {0}: on {1} expected {2}, got: {3}".format(test,num,expected_ans,res)
    assert expected_ans == res, message
    print('ok')
    '''
