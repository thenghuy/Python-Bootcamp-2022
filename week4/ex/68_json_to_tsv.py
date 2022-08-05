import json
import os.path
import pandas as pd
def json_to_tsv(json_file,tsv_file):
  if os.path.exists(json_file):
    x=open(json_file)
    data=json.load(x)
    list1=[]
    list3=[]
    list2=[]
    for j in data["myobj"]:
      title=j["title"]
      list1.append(title)
      content=j["content"]
      list2.append(content)
      difficulty=j["difficulty"]
      list3.append(difficulty)
      data={"title":list1,"content":list2,"difficulty":list3}
      df=pd.DataFrame(data=data)
      df.to_csv(tsv_file)
    return 1
  else:
    return 0
res=json_to_tsv("bc_test.json","bc_test1.csv")
print(res)
