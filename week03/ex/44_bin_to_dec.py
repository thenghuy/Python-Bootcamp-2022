def bin_to_dec(number):
    p = set(str(number))
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        decimal_num=int(str(number),2)
        print(decimal_num)
    else:
        print("This is not a binary number")
bin_to_dec(110011)