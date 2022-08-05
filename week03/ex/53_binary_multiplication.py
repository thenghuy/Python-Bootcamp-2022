def binaryProduct(binaryOne, binaryTwo):
    i = 0
    remainder = 0
    sum = []
    binaryProd = 0
    while binaryOne != 0 or binaryTwo != 0:
        sum.insert(i, (((binaryOne % 10) + (binaryTwo % 10) + remainder) % 2))
        remainder = int(((binaryOne % 10) + (binaryTwo % 10) + remainder) / 2)
        binaryOne = int(binaryOne / 10)
        binaryTwo = int(binaryTwo / 10)
        i = i + 1
    if remainder != 0:
        sum.insert(i, remainder)
        i = i + 1
    i = i - 1
    while i >= 0:
        binaryProd = (binaryProd * 10) + sum[i]
        i = i - 1
    return binaryProd
def binary_multiplication(num1, num2):
    binary_of_num1 = bin(num1).replace("0b", "")
    binary_of_num2 = bin(num2).replace("0b", "")
    binaryMultiply = 0
    factor = 1
    firstBinary = int(binary_of_num1)
    secondBinary = int(binary_of_num2)
    while secondBinary != 0:
        digit = secondBinary % 10
        if digit == 1:
            firstBinary = firstBinary * factor
            binaryMultiply = binaryProduct(firstBinary, binaryMultiply)
        else:
            firstBinary = firstBinary * factor
        secondBinary = int(secondBinary / 10)
        factor = 10

    print("Num1                :  {}\n"
          "Num2                :  {}\n"
          "Product (Binary)    :  {}\n"
          "Product (Decimal)   :  {}".format(binary_of_num1, binary_of_num2, binaryMultiply,num1*num2))
binary_multiplication(50,60)
