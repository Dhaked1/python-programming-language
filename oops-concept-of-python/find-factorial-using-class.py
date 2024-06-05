class myclass:
    def fact(self,x):
        factno = 1
        for i in range(1,x+1):
            factno = factno*i
        print("Factorial:",factno)
object = myclass()
a = int(input("enter a value :"))
object.fact(a)