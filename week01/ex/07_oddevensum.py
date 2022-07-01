num=input("Input a number:")
even_sum=0
odd_sum=0
if num.isdigit():
   num=int(num)
   for j in range(0,num+1):
          if j%2!=0:
              odd_sum=odd_sum+j
   print(f"Sum of odd numbers={odd_sum}")
   for i in range(0,num+1):
          if i%2==0:
             even_sum=even_sum+i
   print(f"Sum of even numbers={even_sum}")
else:
    print("Invalid input")
    print(f"Sum of odd numbers={odd_sum}")
    print(f"Sum of even numbers={even_sum}")


