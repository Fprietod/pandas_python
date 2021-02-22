# Lambda Functions
A function is an object that is able to accept some sort of input, possibly modify it, and return some sort of output. In Python, a lambda function is a one-line shorthand for function. A simple lambda function might look like this:
```python
add_two = lambda my_input: my_input + 2
```
So this code:

```python
print(add_two(3))
print(add_two(100))
print(add_two(-2))
```
Would print:
```shell
>>> 5
>>> 102
>>> 0
```
Let’s break this syntax down:

  -  The function is stored in a variable called add_two
   - lambda declares that this is a lambda function (if you are familiar with normal Python functions, this is similar to how we use def to declare a function)
   - my_input is what we call the input we are passing into add_two
   - We are returning my_input plus 2 (with normal Python functions, we use the keyword return)

Let’s write a lambda function that checks if a string is a substring of the string “This is the master string”.
```python
is_substring = lambda my_string: my_string in "This is the master string"
```
So, the code:
```python
print(is_substring('I'))
print(is_substring('am'))
print(is_substring('the'))
print(is_substring('master'))
```

Would print:
```shell
>>> 5
>>> 102
>>> 0
```
We can do this using an if statement in our lambda function, with syntax that looks like:
```python
<WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>
```
So this is what our check_if_A_grade function might look like:
```python
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'
```
This is what this line of code does:

   - Declare lambda function with an input called grade (lambda grade:)
   - Return 'Got an A!' if this statement is true:
 ```python
 grade >= 90
 ```
 - Otherwise, return 'Did not get an A...' if this statement is not true:
 ```python
 grade >= 90
 ```
 ~~~
 Lambda functions only work if we’re just doing a one line command. If we wanted to something longer, we’d need a more complex function. Lambda functions are great when you need to use a function once. Because you aren’t defining a function, the reusability aspect functions is not present with lambda functions. By saving the work of defining a function, a lambda function allows us to efficiently run an expression and produce an output for a specific task, such as defining a column in a table, or populating information in a dictionary.
 ~~~
