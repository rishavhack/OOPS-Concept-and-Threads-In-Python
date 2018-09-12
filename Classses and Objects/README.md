# Classes and Object

>The entire OOPS methodology has been derived from a single root concept called **Object**. Every object has some behavior. The behavior of an object is represented by attributes and actions. For Example, Let's take a person whose name is 'Rishav'. Rishav is an object because he exists physically. He has attributes like name,age,sex,etc.These attributes can be represented by variables in programming. 
<br>
>Similarly, Rishav can perfrom some action like talking,walking,eating and sleeping etc. These action are performed by methods. We should understand that a function written inside a class is called a method.So an object contain variable and methods.
<br>
>It is possible that some object may have similar behavior. Such object belong to same category called a **Class**.For example, not only Rishav,but all other person have various common attributes and actions.So they are all objects of same class,'Person'. Now observe that the 'Person' will not exist physically but only Rishav,Ravi,Sita etc. exist physically. This means, a class is a group name and does not exist physically, but objects exist physically

## Some import points
>**__init__()** --We can't declare variable in class,So we have written the variable inside a special method,i.e __init__(). This method is useful to initialize the variable. Hence, the name 'init'.
<br>
>**self** --Self is variable that refers to current class instance. when we create an instance for the class, a separate memory block is allocated on the heap and that memory location is by default stored in 'self'.
<br>
'''
class Student(object):
	"""docstring for Student"""
	def __init__(self):
		self.name = 'Rishav'
		self.age = 25
		self.marks = 88

	def talk(self):
		print "Hi I am ",self.name
		print "My age is ",self.age
		print "My marks is ",self.marks

s1  = Student() //instance = className
s1.talk()		
''' 
<br>
Some points on above Code
1.First of all, a block of memory is allocated on heap.How much memory allocated is decided from the attributes and methods available in the Student class.
2.After allcationg the memory block,the special method by the name '__iniy__(self)' is called internally. This method stores the initial data into the variables.Since this method is useful to construct the instance, it is called **Construtor**
3.Finally, the allocated memory location address of the instance is returned intp 's1' variable. To see this memory location in decimal number format, we can use **id()** function as id(s1). 