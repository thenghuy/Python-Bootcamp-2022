def binary_addition(num1,num2):
    binary_num_1=bin(num1).replace("0b","")
    binary_num_2=bin(num2).replace("0b","")
    sum=num1+num2
    binary_sum=bin(sum).replace("0b","")
    print("Num1         :  {}\n"
          "Num2         :  {}\n"
          "Sum (Binary) :  {}\n"
          "Sum (Decimal):  {} ".format(binary_num_1,binary_num_2,binary_sum,sum))
binary_addition(60,50)