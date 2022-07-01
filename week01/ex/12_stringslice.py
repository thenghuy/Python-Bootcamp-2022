string=input("Input a text:")
if string=="":
    print("The string is empty")
else:
    mid=len(string)//2
    print(string[:mid]+string[mid::])