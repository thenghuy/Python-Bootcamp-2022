sum_num=0
while True:
     your_num = input("Input a number:\n")
     if your_num.isdigit():
         if your_num!="stop":
             sum_num=sum_num+int(your_num)
     elif your_num=="stop":
         print(f"Sum={sum_num}")
         break
     else:
         print("The input must be a valid number!")
