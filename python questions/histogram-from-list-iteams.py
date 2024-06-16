def histogram (data):
    for n in data:
        output =""
        time = n
        while (time>0):
            output+="*"
            time -= 1
        print(output)    
        
histogram([2,5,8,9,3,5])







    