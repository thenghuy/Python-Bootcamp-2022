def dec_to_bin(number):
    if number>=1:
        dec_to_bin(number//2)
        print(number%2,end="")
dec_to_bin(50)