class A:
    def funA(self):
        print("welcome to class A")
class B(A):
    def funB(self):
        print("welcome to class B")
class C:
    def funC(self):
        print("welcome to class C")
class D:
    def funD(self):
        print("welcome to class D")
objA=A()
objA.funA()
objB = B()
objB.funA()
objB.funB()
objC = C()
objC.funC()
objD = D()
objD.funD()