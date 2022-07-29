def bin_to_hex(number):
    p = set(str(number))
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        decimaml_number = int(str(number), 2)
        hex_num = hex(decimaml_number).replace("0x", "")
        print(hex_num)
    else:
        print("This is not a binary number")
bin_to_hex(11001101)