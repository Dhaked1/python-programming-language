class destruc:
    def __init__(self):
        print("this is python constructror method:")
    def MYmethod(self):
        print("this is normal method")
    def __del__(self):
        print("welcome to the detructor method of python:")
        print("we have deleted the object")              
obj1 = destruc()
obj1.MYmethod()
del obj1
#obj1.MYmethod() name obj1 is not defined