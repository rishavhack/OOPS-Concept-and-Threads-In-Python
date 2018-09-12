# Classes and Object

>The entire OOPS methodology has been derived from a single root concept called **Object**. Every object has some behavior. The behavior of an object is represented by attributes and actions. For Example, Let's take a person whose name is 'Rishav'. Rishav is an object because he exists physically. He has attributes like name,age,sex,etc.These attributes can be represented by variables in programming. 

>Similarly, Rishav can perfrom some action like talking,walking,eating and sleeping etc. These action are performed by methods. We should understand that a function written inside a class is called a method.So an object contain variable and methods.

>It is possible that some object may have similar behavior. Such object belong to same category called a **Class**.For example, not only Rishav,but all other person have various common attributes and actions.So they are all objects of same class,'Person'. Now observe that the 'Person' will not exist physically but only Rishav,Ravi,Sita etc. exist physically. This means, a class is a group name and does not exist physically, but objects exist physically

## Some import points
>**__init__()** --We can't declare variable in class,So we have written the variable inside a special method,i.e __init__(). This method is useful to initialize the variable. Hence, the name 'init'.

>**self** --Self is variable that refers to current class instance. when we create an instance for the class, a separate memory block is allocated on the heap and that memory location is by default stored in 'self'.

class Student(object):
	def __init__(self):
		self.name = 'Rishav'
		self.age = 25
		self.marks = 88
	def talk(self):
		print "Hi I am ",self.name
		print "My age is ",self.age
		print "My marks is ",self.marks
s1  = Student()
s1.talk()		


## Some points on above Code

1.First of all, a block of memory is allocated on heap.How much memory allocated is decided from the attributes and methods available in the Student class.

2.After allcationg the memory block,the special method by the name '__iniy__(self)' is called internally. This method stores the initial data into the variables.Since this method is useful to construct the instance, it is called **Construtor**

3.Finally, the allocated memory location address of the instance is returned intp 's1' variable. To see this memory location in decimal number format, we can use **id()** function as id(s1). 

**Program 1**
> A Python program to define Student to define Student class and create an object to it. Also, we will call the method and display the student's details.

**Program 2**
>A python program to create Student class with a constructor having more than one parameter.

**Program 3**
>A python program to understand instance variable.

**Program 4**
>A python program to understand class variable or static variable

**Program 5**
>A python programming using a student class with instance methods to process the data of several students.

**Program 6**
>A python program to store data into instances using mutator and to retrieve data from the instances using accessor methods.

**Program 7**
>A python program to use class method to handle the common feature of all the instance of Bird Class

 **Program 8**
>A python program to create a static method that counts the number of instance created for a class.

 **Program 9**
>A python program to create a static method that calculate the square root value of a given number.

**Program 10**
>A python program to create a Bank class where deposite and withdrawals can be handled by using instance methods.

**Program 11**
>A python program to create Emp class and make all the members of the Emp class avaiable to another class

**Program 12**
>A python program to calculate power value of a number with the help of a static method.

**Program 13**
>A python program to create Dob class within Person class.

**Program 14**
>A python program to create another verison of Dob class within Person class.    