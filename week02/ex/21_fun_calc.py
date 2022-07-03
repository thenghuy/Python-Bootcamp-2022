def fun_calc(num1,num2,operator):
    if operator=="+":
        sum=num1+num2
        print("Product:",sum)
        print("Process:",num1,operator,num2,"=",sum)
    elif operator=="-":
        substract=num1-num2
        print("Product:",substract)
        print("Process:",num1,operator,num2,"=",substract)
    elif operator=="*":
        multi=num1*num2
        print("Product:",multi)
        print("Process:",num1,operator,num2,"=",multi)
    elif operator=="/":
        divide=num1/num2
        print("Product:",divide)
        print("Process:",num1,operator,num2,"=",divide)
fun_calc(50,2,"*")
