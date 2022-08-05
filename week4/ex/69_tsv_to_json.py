import csv
import json
import os
def tsv_to_json(tsv_file,json_file):
 if os.path.exists(tsv_file):
   x=open(tsv_file)
   df=csv.DictReader(x)
   list=[]
   for i in df:
        list.append(i)
   y=open(json_file,"w")
   jsonstring=json.dumps(list,indent=4)
   y.write(jsonstring)
   return 1
 else:
  return 0
res=tsv_to_json("bc_test1.csv","bc_test2.json")
print(res)



