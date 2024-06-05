class hello:
    def fun1(self):
        print("hi")
    @classmethod
    def fun2(cls):
        print("hi ,this is the class method")
    @staticmethod
    def fun3():
        print("hi,this is staticmethod")
obj = hello()
obj.fun1()
#call by class name
hello.fun2()                
hello.fun3()
print("\n")
#call by object name
obj.fun2()
obj.fun3()