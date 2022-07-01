sum_of_the_given_numbers=0
while True:
     your_num = input("Input a number:\n")
     if your_num.isdigit():
         if your_num!="stop":
             sum_of_the_given_numbers=sum_of_the_given_numbers+int(your_num)
     elif your_num=="stop":
         print(f"The sum is={sum_of_the_given_numbers}")
         break
     else:
         print("The input must be a valid number!")
