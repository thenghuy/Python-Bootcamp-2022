def myfunc():
    option = int(input("Press 1 to encode\nPress 2 to encode\n"))
    string = input("Enter your string to encode:\n")
    new_string = ""
    for i in range(len(string)):
        n = ord(string[i])
        if option==1:
            if n>=65 and n<=77:
              n=n+13
              new_string=new_string+chr(n)
            else:
               n=n-13
               new_string=new_string+chr(n)
        elif option==2:
            if n>=77 and n<=90:
               n=n-13
               new_string=new_string+chr(n)
            else:
               n=n+13
               new_string=new_string+chr(n)
    print("The decoded text is:",new_string)
myfunc()
while True:
    question = input("Do you want to continue?[Y/N]\n")
    if question == "N":
        break
    elif question=="Y":
        myfunc()
