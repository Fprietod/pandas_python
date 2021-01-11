#A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. 
#We used the pass keyword in Python to indicate that the body of the class was intentionally left blank so we don’t cause an IndentationError
class CoolClass:
  pass
  
 
 #Instantiation

#A class doesn’t accomplish anything simply by being defined.

cool_instance = CoolClass()
#Object-Oriented Programming
#In Python __main__ means “this current file that we’re running” and so one could read the output from type()
#You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
class Musician:
  title = "Rockstar"
 
drummer = Musician()
print(drummer.title)
# prints "Rockstar"

