def or_operation(hexa1,hexa2):
    decimal1=int(hexa1,16)
    decimal2=int(hexa2,16)
    binary1=bin(decimal1).replace("0b","")
    binary2 = bin(decimal2).replace("0b", "")
    print(binary1)
    print(binary2)
    sum=str(int(binary1)+int(binary2))
    for i in sum:
        if i=='0':
            sum='0'
        elif i=='1':
            sum='1'
        elif i=='2':
            sum='1'
        print(sum,end="")
or_operation("33","3D")