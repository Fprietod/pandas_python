#Let’s start with and.
#and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise
#Oranges are a fruit and carrots are a vegetable.
#This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, both of which are True and connected by the boolean operator and, so the entire expression is True.
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa >=2.0:
    return "You meet the requirements to graduate!"
