string=input("Input a string:")
if string=="":
    print("The string is empty")
else:
    mid=len(string)//2
    firsthalf=string[:mid]
    secondhalf=string[mid::]
    print(firsthalf[::-1]+secondhalf)
