def dec_to_oct(number):
    if number>=1:
        dec_to_oct(number//8)
        print(number%8,end="")
dec_to_oct(98)