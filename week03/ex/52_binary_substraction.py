def binary_substraction(num1,num2):
    binary_of_num1=bin(num1).replace("0b","")
    binary_of_num2 = bin(num2).replace("0b", "")
    substraction=num1-num2
    binary_of_sunstraction=bin(substraction).replace("0b", "")
    print("Num1                :  {}\n"
          "Num2                :  {}\n"
          "Difference (Binary) :  {}\n"
          "Difference (Decimal):  {} ".format(binary_of_num1,binary_of_num2,binary_of_sunstraction,substraction))
binary_substraction(60, 50)