class A:
    def funA(self):
        print("welcome to class A")
class B(A):
    def funB(self):
        print("welcome to class B")
class C(B):
    def funC(self):
        print("welcome to class C")
class D:
    def funD(self):
        print("welcome to class D")                        
obj = C()
obj.funC()
obj.funB()
obj.funA()