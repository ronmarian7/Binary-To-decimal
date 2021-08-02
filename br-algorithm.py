
def br(x, k):
## x is the decimal num and k is the amont of bits
    x = int(x)
    k = int(k)
    if x >= 2**k:
        return f"You can not convert {x} by {k} bits"
    if k == 1:
        return f'{int(x)}'
    if x % 2 == 0:
        return br(x/2, k-1) + '0'
    else:
        return br((x-1)/2, k-1) + '1'


def from_b_to_d(x):
    x = int(x)
    binary_str = str(x)[::-1]
    decimal_sum = 0
    for i in range(len(binary_str)):
        decimal_sum += int(binary_str[i])*(2**i)
    return decimal_sum


stat = False
while not stat:
    choice = input('If you want to convert decimal num into binary type decimal,\n'
                'if you want from binary to decimal type binary:')
    choice = choice.strip().lower()
    if choice == 'decimal':
        opp = input('Please enter the decimal number you want to convert and the amount of bits: ')
        x, k = opp.strip().split()
        print(f'The binary representation of {x} with {k} bits is:', br(x, k))
        stat = True
    elif choice == 'binary':
        opp = input('Please enter the binary number you want to convert: ')
        x = opp.strip()
        print(f'The decimal representation of {x} is:', from_b_to_d(x))
        stat = True












