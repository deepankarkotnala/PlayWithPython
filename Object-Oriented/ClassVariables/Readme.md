```python

class Employee():

    num_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = str(self.fname + '.' + self.lname + '@companyname.com').lower()

        # This is a class variable because we don't want to reset this value for every instance.
        # Also, we don't want this value to be overwritten by any of the subclass 
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Deepankar','Kotnala',10_00_000)
emp2 = Employee('Test','Employee',10_000)

print('\n=================================')
print('Mail id: ', emp1.email)
print('Pay before raise: ',emp1.pay)
emp1.applyraise()
print('Employee 1 pay after raise: ', emp1.pay)

emp1.raise_amount = 1.05
print('Employee 1 instance raise_amount changed to 1.05\nSo the value of emp1.raise_amount now is: ', emp1.raise_amount)
print('Employee 2 raise_amount instance variable value is: ',emp2.raise_amount)
print('Number of Employees: ', Employee.num_of_employees)

print(emp1.__dict__, '\n')
print(Employee.__dict__,'\n')

```

