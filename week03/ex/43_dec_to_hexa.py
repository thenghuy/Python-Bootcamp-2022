def dec_to_hexa(number):
    if number>=1:
        dec_to_hexa(number//16)
        remainder=number%16
        if remainder==10 :
            remainder="A"
        elif remainder==11:
            remainder="B"
        elif remainder==12:
            remainder="C"
        elif remainder==13:
            remainder="D"
        elif remainder==14:
            remainder="E"
        elif remainder==15:
            remainder="F"
        elif remainder==16:
            remainder="G"
        print(remainder,end="")
dec_to_hexa(1500)

