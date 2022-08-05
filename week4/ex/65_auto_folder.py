import os
def create_new_folder(foldername):
     parent_path="C:/Users/keoly/OneDrive/Desktop/Python Bootcamp 2022/week4"
     path=os.path.join(parent_path,foldername)
     os.mkdir(path)
def autofolder(foldername):
    isfolder=os.path.isdir(foldername)
    if isfolder==False:
      while True:
       question=input(f"Are you sure you want replace {foldername}?[Y/N]")
       if question=="Y" or question=="y":
         create_new_folder(foldername)
         return 1
       elif question == "N" or question == "n":
         return 0
       else:
        print("Invalid option")
    else:
        return 0
res=autofolder("Test folder1")
print(res)
