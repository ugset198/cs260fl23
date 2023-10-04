from icecream import ic
from lab1 import weighted_sum
# note: if icecream is not installed
# in terminal execute:
#    pip install icecream 

lookup_table1 = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15
}

lookup_table2 = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'a',
    11:'b',
    12:'c',
    13:'d',
    14:'e',
    15:'f'
}
def repeated_div(num: str, base: int):
    Q = weighted_sum(num) # int(num)
    R = 0
    result = ''

    while Q !=0:
        R = Q % base
        Q = Q // base
        result = lookup_table2[ R ] + result
        # result = f'{R}{result}'
    return result

ic( repeated_div('11' , 2) )

