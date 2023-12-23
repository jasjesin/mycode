import uuid


class Student:
    def __init__(self, fn, ln, dept):
        self.sid = uuid.uuid4().hex
        self.fn = fn
        self.ln = ln
        self.dept = dept

    def __str__(self):
        return f'ID: {self.sid}\n' \
               f'First Name: {self.fn}\n' \
               f'Last Name: {self.ln}\n' \
               f'Department: {self.dept}'


student = Student("Jas", "Singh", "get a Job")
print(student)
