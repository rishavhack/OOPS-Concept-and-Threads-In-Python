#Using Teacher class
from Program1 import Teacher

#Create instance
t = Teacher()
t.setid(10)
t.setname('Rishav')
t.setaddress('SGR Dental')
t.setSalary(25000)


#Reterive value from insatance and display
print 'id = ',t.getid()
print 'name = ',t.getname()
print 'address =',t.getaddress()
print 'salary =',t.getSalary() 