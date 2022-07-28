def oct_to_dec(number):
    for ch in str(number):
       if (ch < '0' or ch > '7') :
            print("This is not an octal number")
            return
    decimal_num = int(str(number), 8)
    print(decimal_num)
oct_to_dec(750)

