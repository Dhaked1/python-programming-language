class A:
    def __funa(self):
        print("hello i can accessible by creating object inside the class")
    def normalmethod(self):
        print("hello i can accessible by creating object outside the class")
        objecta = A()    
        objecta.__funa()
class B(A):
    def funB(self):
        print("welcome to class B")                
objectA = A()
objectA.normalmethod()