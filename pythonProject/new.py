from employee import Employee
from address import address
address1=address("banglore")
address2=address("hyderabad")

emp1=Employee("Jaishu","Nani","vijayawada")
emp2=Employee("Jaishu","Nani",[address1,address2])
print(address1.display())
print(address2.display())
print(emp1.display())
print(emp2.display())
