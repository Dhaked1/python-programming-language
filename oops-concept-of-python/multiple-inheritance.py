class a:
    def funa(self):
        print("welcome to class a")
class b():
    def funb(self):
        print("welcome to class b")
class c():
    def func(self):
        print("welcome to class c")
class d(a,b,c):
    def fund(self):
        print("welcome to class d")
obj = d()        
obj.fund()
obj.func()
obj.funb()
obj.funa()