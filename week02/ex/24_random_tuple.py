import random
def random_tuple(n):
    list=[]
    sum = 0
    x = random.sample(range(0, 100), n)
    for i in range(n):
        list.append(x[i])
        sum = sum + x[i]
        print(f"random number{i+1}:",x[i])
    print(tuple(list))
    print(sum)
random_tuple(5)
