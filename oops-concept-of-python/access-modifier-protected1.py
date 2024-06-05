#only inherited class can access it
#_ makes it protected
class a:
    def _funa(self):
        print("welcome to class A:")
class b(a):
    def funb(self):
        print("welcome to class B")
objectb =b()
objectb._funa()