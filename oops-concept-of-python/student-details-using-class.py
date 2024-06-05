class studentrecord:
    def studentdetails(self,name,rollno):
        print("Name of the student is:",name)
        print("Roll number of the student is:",rollno)
    def studentresult(self,marks,percentage):
        print("Marks of the student is :",marks)
        print("Percentage of the student is :",percentage)
stu1 = studentrecord()            
stu1.studentdetails("ram",8798)
stu1.studentresult(210,90)
stu2 = studentrecord()
stu2.studentdetails("shyam",5567)
stu2.studentresult(243,91)