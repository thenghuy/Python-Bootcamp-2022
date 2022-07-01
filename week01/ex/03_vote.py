yourage=int(input("Input your age:"))
if yourage>0:
    if yourage>=18:
        print("You are eligible to vote ")
    else:
        print("You aren't adult yet...Sorry you can't vote")
else:
    print("Age must be a positive digit.")