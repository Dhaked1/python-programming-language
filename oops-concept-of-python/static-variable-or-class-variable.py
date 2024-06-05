class studentrecord:
    studentname = "alka dhakad"
    def studentdetails(self,name,rollno):
        self.a = name
        self.b = rollno
    def display_details(self):
        print("Name of the student is:",self.a)
        print("Roll number of the student is :",self.b)
stu1 = studentrecord()            
stu1.studentdetails("kunal",112223)
stu1.display_details()
print("static variable:",stu1.studentname)

stu2 = studentrecord()            
stu2.studentdetails("ram",254)
stu2.display_details()
print("static variable:",stu2.studentname)
new = stu2.studentname = "alka dhakad  changed for this object only for rest of the object it will be same"
print("static variable changed",new)