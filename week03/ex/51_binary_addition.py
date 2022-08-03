def binary_addition(num1,num2):
    binary_num_1=bin(num1).replace("0b","")
    binary_num_2=bin(num2).replace("0b","")
    list=[]
    c="0"
    maxlength=max(len(binary_num_1),len(binary_num_2))
    binary_num_1=binary_num_1.zfill(maxlength)
    binary_num_2=binary_num_2.zfill(maxlength)
    for i in range(maxlength-1,-1,-1):
           b1=binary_num_1[i]
           b2 = binary_num_2[i]
           if b1=="0" and b2=="0" and c=="0":
             list.append("0")
             c="0"
           elif b1 == "1" and b2 == "1" and c == "1":
             list.append("1")
             c = "1"
           elif (b1 == "1" and b2 == "0" and c == "0")or (b1 == "0" and b2 == "1" and c == "0") or (b1 == "0" and b2 == "0" and c == "1"):
             list.append("1")
             c = "0"
           else:
             list.append("0")
             c = "1"
    if c=="1":
           list.append("1")
    result="".join(list[::-1])
    print("Num1                :  {}\n"
          "Num2                :  {}\n"
          "Difference (Binary) :  {}\n"
          "Difference (Decimal):  {} ".format(binary_num_1,binary_num_2,result,num1+num2))
binary_addition(60,50)


