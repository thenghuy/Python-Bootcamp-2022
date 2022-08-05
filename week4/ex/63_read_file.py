import os
def read_file(path ):
 if os.path.exists(path):
  file=open(path,"r")
  print(file.read())
  file.close()
 else:
  print("File is not exist!")
read_file("read_file.txt")