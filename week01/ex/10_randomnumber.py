import random
no_of_num=int(input("Input number:"))
n=random.sample(range(2000,3000),no_of_num)
sum=0
for i in n:
    if i%2==0:
        sum=sum+i
print(f"Sum of even random numbers:{sum}")