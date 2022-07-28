def hex_to_oct(number):
    for ch in number.upper():
        if ((ch < '0' or ch > '9') and  (ch < 'A' or ch > 'F')):
            print("This is not a hexa-decimal number")
            return
    decimal = int(number, 16)
    oct_num = oct(decimal).replace("0o", "")
    print(oct_num)
hex_to_oct("2b9")