class a:
    def _funa(self):
        print("welcome to class A:")
class b(a):
    def funb(self):
        objecta = a()
        objecta._funa()
objectb =b()
objectb.funb()
