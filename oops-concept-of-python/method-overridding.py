class A:
    def funa(self):
        print("welcome to class A")
class B(A):
    def  funa(self):
        print("welcome to class B")
    def funb(self):
        print("hello!")          
obj1 = A()
obj1.funa()
obj2 = B()
obj2.funa()
obj2.funb()