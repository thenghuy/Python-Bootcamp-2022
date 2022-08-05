import os
def delete_file(filename):
  if os.path.exists(filename):
    while True:
     question=input(f"Are you sure you want delete {filename}?[Y/N]")
     if question=="Y" or question=="y":
             parent_path = "C:/Users/keoly/OneDrive/Desktop/Python Bootcamp 2022/week4"
             path = os.path.join(parent_path, filename)
             os.remove(path)
             return 1
     elif question == "N" or question == "n":
       return 0
     else:
       print("Invalid option")
  else:
      return 0
res=delete_file("ss.txt")
print(res)