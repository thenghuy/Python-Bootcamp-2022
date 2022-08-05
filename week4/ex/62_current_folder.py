import os
def current_folder(current_path):
 list=[]
 for (root, dirs, files) in os.walk(current_path):
    for i in range(len(files)):
           x=files[i], " files "
           list.append(x)
    for j in range(len(dirs)):
           y=dirs[j],"folder"
           list.append(y)
 print(list)
current_folder("C:/Users/keoly/OneDrive/Desktop/Python Bootcamp 2022/week4")