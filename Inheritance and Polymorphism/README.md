# Inheritance and Polymorphism
>Creating new classes from existing classes, so that the new classes will acquire all the features of the existing classes is called **Inheritance**. A good example for inheritance in nature is parents producing the children and children inheriting the qualities of the parents.

### Example

```
Class A:
	a = 1
	b = 2
	def method(cls):
		print cls.a
		print cls.b
class B:
	c = 3
	def method2(cls):
		print cls.c
```

# Polymorphism
>The word 'Polymorphism' came from two Greek words 'Poly' meaning 'many' and 'morphos' meaning 'forms'. Thus,Polymorphism represented the ability to assume several different forms. In Programming, if an object or method is exhibiting different behavior in different contexts,it is called Polymorphic nature

### Example - Below function is performing two different tasks,it said to exhibit polymorphism
```
#a function that exhibits polymorphism
def add(a,b):
	print a+b

#Call add() and pass integer	
add(5,10)
#Call add() and pass strings
add("Core","Python")
```


### Below program is based on setter() and getter()
>A programmer in the software development is creating Teacher class with setter() and gett() method as shown in Program 1. Then be saved this code in a file 'Teacher.py'
**Program 1**
>A python program to create Teacher class and store it into Program 1.py module