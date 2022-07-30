def binary_multiplication(num1,num2):
    binary_of_num1=bin(num1).replace("0b","")
    binary_of_num2 = bin(num2).replace("0b", "")
    multiplication=num1*num2
    binary_multi=bin(multiplication).replace("0b", "")
    print("Num1                :  {}\n"
          "Num2                :  {}\n"
          "Product (Binary)    :  {}\n"
          "Product (Decimal)   :  {} ".format(binary_of_num1,binary_of_num2,binary_multi,multiplication))
binary_multiplication(60, 50)