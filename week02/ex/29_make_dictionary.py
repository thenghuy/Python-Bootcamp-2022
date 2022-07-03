def make_dictionary(list,tuple):
 dict={}
 for i in range(0,len(list)):
   x={list[i]:tuple[i]}
   dict.update(x)
 print(dict,end="")
make_dictionary([50,10,62],("Borey","Thirak","Dane"))

