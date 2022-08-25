class student:
    def __init__(self,student_id,student_name):
        self.id=student_id
        self.name=student_name
    def getstddet(self):
        return self.id , self.name
st1=student(22794,'jaishu')
display=st1.getstddet()
print(display)
setattr(st1,'student_class',1)
print(getattr(st1,'student_class'))
delattr(st1,'name')
print(hasattr(st1,'student_name'))
st1=student(22794,'jaishu')
display=st1.getstddet()
print(display)



