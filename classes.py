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


#Methods are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method.
#Convention recommends that we name this first argument self
class Dog:
  dog_time_dilation = 7
 
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
 
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
#When you call a method it automatically passes the object calling the method as the first argument.

#Methods with Arguments
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"
#Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers.
#Notice again that even though how_many_kms takes two arguments in its definition, we only pass miles, because self is implicitly passed
class Circle:
  pi  = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2


circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11.460/2)

#Constructor
#The first dunder method we’re going to use is the __init__() method (note the two underscores before and after the word “init”). 
# This method is used to initialize a newly created object.
# It is called every time the class is instantiated.
class Shouter:
  def __init__(self):
    print("HELLO?!")
 
shout1 = Shouter()
# prints "HELLO?!"
 
shout2 = Shouter()

#We absolutely can, and those parameters will be received by the __init__() method.
#Another example
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
 
      # then shout it out
      print(phrase.upper())
 
shout1 = Shouter("shout")
# prints "SHOUT"
 
shout2 = Shouter("shout")
# prints "SHOUT"
 
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

#Instance variables
#The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class 
#We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

class FakeDict:
  pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)

#Attribute Functions
#hasattr() will return True if an object has a given attribute and False otherwise
# If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute.
#hasattr(object, “attribute”) has two parameters:

  #  object : the object we are testing to see if it has a certain attribute
  #  attribute : name of attribute we want to see if it exists
  
  
# getattr(object, “attribute”, default) has three parameters (one of which is optional):
  
  
  
  #  object : the object whose attribute we want to evaluate
 #   attribute : name of attribute we want to evaluate
 #   default : the value that is returned if the attribute does not exist (note: this parameter is optional)
  
  
 hasattr(attributeless, "fake_attribute")
# returns False
 
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

#has the attribute fake_attribute. Since it does not, hasattr() returned False.
# After that, we used getattr to attempt to retrieve other_fake_attribute.
#  Since other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.
#Example when have a count for attribute
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
    
 
#Self
#Since the self keyword refers to the object and not the class being called
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.url)
# prints "www.codecademy.com"
 
print(wikipedia.url)
# prints "www.wikipedia.org"

#we can define a secure method on the SearchEngineEntry class that returns the secure link to an entry.

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.secure())
# prints "https://www.codecademy.com"
 
print(wikipedia.secure())
# prints "https://www.wikipedia.org"

#Above we define our secure() method to take just the one required argument, self. We access both the class variable self.secure_prefix and the instance variable self.url to return a secure URL. 
#Another example
class Circle:
  pi = 3.14
  def __init__(self, diameter):

    print("Creating circle with diameter {d}".format(d=diameter))
    
    # Add assignment for self.radius here:
    self.radius = diameter/2
  def circumference(self):
    return 2 * self.pi * self.radius
   
  


medium_pizza =Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())



