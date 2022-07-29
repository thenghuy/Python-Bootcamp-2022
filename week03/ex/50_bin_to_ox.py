def bin_to_oct(number):
    p = set(str(number))
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        decimal = int(str(number), 2)
        octal_num = oct(decimal).replace("0o", "")
        print(octal_num)
    else:
        print("This is not a binary number")
bin_to_oct(11001101)