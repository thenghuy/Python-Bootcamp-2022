def hex_to_dec(number):
    for ch in number.upper():
        if ((ch < '0' or ch > '9') and  (ch < 'A' or ch > 'F')):
            print("This is not a hexa-decimal number")
            return
    decimal_num = int(number, 16)
    print(decimal_num)
hex_to_dec("BA1")
