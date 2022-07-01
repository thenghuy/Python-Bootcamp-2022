your_num=input("Input a number:")
if your_num.isdigit():
    if int(your_num)%2==0:
        print("The number you have entered is Even")
    else:
        print("The number you have entered is Odd")
else:
    print("Not a valid Number")


