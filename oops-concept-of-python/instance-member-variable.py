class studentrecord:
    def studentdetails(self,name,rollno):
        self.a = name
        self.b = rollno
    def studentresult(self,marks,percentage):
        self.c = marks
        self.d = percentage
    def display_details(self):
        print("name of the student is :",self.a)
        print("roll number of the studebnt is :",self.b)
    def display_result(self):
        print("marks of studentis: ",self.c)
        print("percentage of student is",self.d)
stu = studentrecord()
stu.studentdetails("alka",5)
stu.studentresult(23435,99)
stu.display_details()
stu.display_result()