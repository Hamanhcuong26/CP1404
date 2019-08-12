re_times = int(input('How many times you would like to enter: '))


def get_number(lower, upper):
    if in_number >= lower & in_number <= upper:
        return True
    else:
        return False


for i in range(re_times):
    # char to ascii
    in_char = input('Enter a character: ')
    print('The ASCII code for {} is {}'.format(in_char, ord(in_char)))

    # ascii to char
    in_number = int(input('Enter a number between 33 and 127: '))
    if get_number(33, 127):
        print('The character for {} is {}'.format(in_number, chr(in_number)))
    else:
        print('Not valid number!')
        number = input('Enter a number between 33 and 127: ')
    print('---------')
print('---Finish---')
