class Employee():

    raise_amount = 1.04
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = str(self.fname + '.' + self.lname + '@companyname.com').lower()

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def applyraise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp1 = Employee('Deepankar','Kotnala',10_00_000)
emp2 = Employee('Test','Employee',10_000)

print('\n=================================')
print(emp1.email)
print(emp1.pay)
emp1.applyraise()
print(emp1.pay)

emp1.raise_amount = 1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print(emp1.__dict__, '\n')
print(Employee.__dict__,'\n')
