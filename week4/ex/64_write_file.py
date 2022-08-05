import os
def create_new_file(filename,content):
  file=open(filename,"w")
  file.write(content)
  file.close()
  return 1
def writefile(filename,content):
 if os.path.exists(filename):
  while True:
   question=input(f"Are you sure you want replace {filename}?[Y/N]")
   if question=="Y" or question=="y":
    create_new_file(filename,content)
    return 1
   elif question == "N" or question == "n":
    return 0
   else:
    print("Invalid option")
  else:
   create_new_file(filename,content)
   return 1
res=writefile("read_file.txt","aewaerwrewqreewqh")
print(res)


