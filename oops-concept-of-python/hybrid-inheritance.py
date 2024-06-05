class a:
    def funa(self):
        print("welcome to class a")
class b(a):
    def funb(self):
        print("welcome to class b")
class c(a):
    def func(self):
        print("welcome to class c")
class d(b,c):
    def fund(self):
        print("welcome to class d")
obj1 = d()        
obj1.fund()
obj1.func()
obj1.funb()
obj2 = b()
obj2.funb()
obj2.funa()
obj3 = c()
obj3.func()
obj3.funa()