#Let’s start with and.
#and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise
#Oranges are a fruit and carrots are a vegetable.
#This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, both of which are True and connected by the boolean operator and, so the entire expression is True.
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa >=2.0:
    return "You meet the requirements to graduate!"

  # OR
  #Oranges are a fruit or apples are a vegetable.
  #This statement is composed of two expressions: oranges are a fruit which is True and apples are a vegetable which is False.
  #Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True.
  
  #Operator Not
  #So if we have a True statement and apply a not operator we get a False statement.
  #not True == False
  #not False == True
  >>> not 1 + 1 == 2
False
>>> not 7 < 0
True
#####################
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"
