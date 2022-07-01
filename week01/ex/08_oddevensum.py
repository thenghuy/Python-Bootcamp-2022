num=input("Input a number:")
even_sum=0
odd_sum=0
if num.isdigit():
   num=int(num)
   for j in range(0,num+1):
          if j%2!=0:
              odd_sum=odd_sum+j
              average_odd = odd_sum / (num / 2)
   print(f"Average of odd numbers={average_odd}")
   for i in range(0,num+1):
          if i%2==0:
             even_sum=even_sum+i
             average_even=even_sum/(num/2)
   print(f"Average of even numbers={average_even}")
else:
    print("Invalid input")