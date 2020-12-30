#lambda function is a one-line shorthand for function.
add_two = lambda my_input: my_input + 2
print(add_two(3))
print(add_two(100))
print(add_two(-2))
#The print
 5
>>> 102
>>> 0
#Explain the function
#1. The function is stored in a variable called add_two
# 2. lambda declares that this is a lambda function (if you are familiar with normal Python functions, this is similar to how we use def to declare a function)
# 3. my_input is what we call the input we are passing into add_two
# 4. We are returning my_input plus 2 (with normal Python functions, we use the keyword return)
# Example Let’s write a lambda function that checks if a string is a substring of the string “This is the master string”.
# Code
is_substring = lambda my_string: my_string in "This is the master string"

#The code
print(is_substring('I'))
print(is_substring('am'))
print(is_substring('the'))
print(is_substring('master'))
#Would print
>>> False
>>> False
#We can do this using an if statement in our lambda function, with syntax that looks like:
#<WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>
#So this is what our check_if_A_grade function might look like:
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'
#1: Declare lambda function with an input called grade (lambda grade:)
# Return 'Got an A!' if this statement is true:
grade >= 90
#Otherwise, return 'Did not get an A...' if this statement is not true:
grade >= 90
#Lambda functions only work if we’re just doing a one line command. If we wanted to something longer, we’d need a more complex function. Lambda functions are great when you need to use a function once.
#Create a lambda function named contains_a that takes an input word and returns True
contains_a = lambda word:  'a' in word
print contains_a("banana")
#Function that calculate the len of a word and its neccesary to be hight than 12
long_string  = lambda word: len(word) > 12
#You can get a character of a string string_name by using the syntax string_name[index]
#where index is the place of character you want to get, starting at 0.
#Example
my_string = "Whoa! A seesaw"
print(my_string[0])
#Create a lambda function named ends_in_a that takes an input str and returns True if the last character in the string is an a. Otherwise, return False
ends_in_a = lambda word: 'a' in word[-1]
#The last character in the string is string_name[-1].
#As a reminder, to return different output depending on different input, we can use if and else inside our lambda function:
add_or_subtract = lambda input_number: input_number - 1 if input_number >= 0 else input_number + 1
#Another 
double_or_zero = lambda num: num * 2 if num > 10 else 0
