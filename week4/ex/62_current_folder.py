import os
list=[]
for (root, dirs, files) in os.walk("C:/Users/keoly/OneDrive/Desktop/Python Bootcamp 2022/week4"):
    for i in range(len(files)):
           x=files[i], " files "
           list.append(x)
    for j in range(len(dirs)):
           y=dirs[j],"folder"
           list.append(y)
print(list)