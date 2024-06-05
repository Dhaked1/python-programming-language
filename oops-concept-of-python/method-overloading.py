class a:
    def funA(self,x = None,y = None):
        if x==None and y == None:
            print("hello! its example of folymorphism")
        elif x!= None and y == None:
            f = 1
            for i in range(1,x+1):
                f = f*i
            print(f)        
        else:
            print("Addition of number is :",x+y)

obj = a()
obj.funA()
obj.funA(5)
obj.funA(5,6)