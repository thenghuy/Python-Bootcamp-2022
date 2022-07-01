my_string=input("Input a string:")
if my_string=="":
    print("The string is empty.")
else:
    n=my_string.split(" ",8)
    for i in range(1,len(n)):
        x=n[i]
        new_string=n[0].upper()+n[i].lower()
    print(new_string)
    print(x)

