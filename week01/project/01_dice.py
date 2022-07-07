import random
INTRO_MESSAGE="Welcome to the dices game"
print(INTRO_MESSAGE)
number_of_dices_times = input("Enter the number of dices you want to roll:\n")
def game():
    n=int(number_of_dices_times)
    sum = 0
    list=[]
    if n>=1 and n<=8:
       for i in range(n):
           x=random.randint(1,6)
           list.append(int(x))
       for j in range(len(list)):
           sum=sum+list[j]
           print(f"Dice {j + 1}: {list[j]}")
    print("="*10)
    print("Result",sum)
    print("=" * 10)
while True:
 if number_of_dices_times.isdigit() :
     n = int(number_of_dices_times)
     if n >= 1 and n <= 8:
      game()
      break
     elif n>8:
      print("Usage:The number must be between 1 and 8")
      number_of_dices_times = input("Enter the number of dices you want to roll:\n")
      game()
      break
 else:
     print("Usage:The number must be between 1 and 8")
     number_of_dices_times = input("Enter the number of dices you want to roll:\n")
     game()
     break

