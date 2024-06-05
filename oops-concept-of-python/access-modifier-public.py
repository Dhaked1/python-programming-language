class A:
    def funA(self):
        print("welcome to class A:")
class B(A):
    def funB(self):
        print('welcome to class B:')
        object = A()
        object.funA()

objectA = A()
objectA.funA()
objectB = B()
objectB.funB()