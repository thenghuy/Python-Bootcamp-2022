from datetime import datetime
x=open("testfile.txt","a")
while True:
    text=input("$:")
    now=datetime.now()
    d = now.strftime("%d/%b/%Y/ %H:%M:%S")
    content="[{}] {}".format(d,text)
    if text=="exit":
        break
    else:
        x.write(content)
