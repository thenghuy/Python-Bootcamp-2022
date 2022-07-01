string=input("Enter your string here:")
new_string=""
if string=="":
    print("Empty")
else:
 for i in range(len(string)):
  n=ord(string[i])
  if n>=65 and n<=90:
     new_string=new_string+chr(n+32)
  else:
     new_string=new_string+chr(n-32)
print(new_string)
