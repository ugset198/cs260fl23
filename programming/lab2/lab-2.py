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

def add_two_numbers_(num1, num2, base):

    num2 = num2.zfill(len(num1))
    num1 = num1.zfill(len(num2))

    index = len(num1) -1
    carry = 0
    result = ""
    while index >= 0:
        digit1 = lookup_table1 [num1[index]]
        digit2 = lookup_table1 [num2[index]]

        sum_of_digits = digit1 + digit2 + carry

        if sum_of_digits >= base:
            carry = 1
        else:
            carry = 0

        result = lookup_table2[ sum_of_digits % base ] + result

        index -= 1

    # conditionally include carry after the loop terminates
    if carry == 1:
        result = '1' + result 

    return result


base = 2
num1 = "1111"
num2 = "11"
print ('in base:', base, " given two numbers ",  num1,"+",num2 ," the result is ", add_two_numbers_(num1, num2, base))
print()

base = 8
num1 = "775"
num2 = "4"
print ('in base:', base, " given two numbers ", num1,"+",num2 ," the result is ", add_two_numbers_(num1, num2, base))
print()

base = 10
num1 = "95"
num2 = "6"
print ('in base:', base, " given two numbers ", num1,"+",num2 ," the result is ", add_two_numbers_(num1, num2, base))
print()

base = 16
num1 = "fe"
num2 = "3"
print ('in base:', base, " given two numbers ",  num1,"+",num2 ," the result is ", add_two_numbers_(num1, num2, base))
print()

