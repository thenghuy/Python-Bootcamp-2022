def mean_of_list(list):
    sum=0
    n=len(list)
    for i in range(n):
        sum=sum+list[i]
        mean=sum/n
    return mean
res=mean_of_list([50,10,62,32])
print(res)