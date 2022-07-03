def make_list(*string):
    list=[]
    for i in range(len(string)):
        list.append(string[i])
    return list
res=make_list(21,"hello",45)
print(res)