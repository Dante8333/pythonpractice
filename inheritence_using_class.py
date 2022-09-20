class person():

    def __init__(self,name,znumber):
        self.name = name
        self.znumber=znumber

    def show(self):
        print("name of student: ",self.name)
        print("college id: ",self.znumber)

class subjects(person):
    def __init__(self,name,znumber,subject1,subject2,subject3):
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

        person.__init__(self,name,znumber)
    
    def subjectdetails(self):
        print("subject1 = ",self.subject1)
        print("subject2 = ",self.subject2)
        print("subject3 = ",self.subject3)

a = subjects('dante','Z87359','deeplearning','a.i in medical healthcare','iot')

a.show()
a.subjectdetails()