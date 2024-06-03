#in this method we have no need to close the file because file will get close automaticlly
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data")
    
