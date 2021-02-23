# List in python
We’ve seen that the items in a list can be numbers or strings. They can also be other lists!

Once more, let’s return to our class height example:

   - Jenny is 61 inches tall
  -  Alexus is 70 inches tall
  -  Sam is 67 inches tall
  -  Grace is 64 inches tall

Previously, we saw that we could create a list representing both Jenny’s name and height:
```python
jenny = ['Jenny', 61]
```
We can put several of these lists into one list, such that each entry in the list represents a student and their height:
```python
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64]]
```
## zip
Again, let’s return to our class height example:

  -  Jenny is 61 inches tall
  -  Alexus is 70 inches tall
  -  Sam is 67 inches tall
  -  Grace is 64 inches tall

Suppose that we already had a list of names and a list of heights:
```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
```
If we wanted to create a list of lists that paired each name with a height, we could use the command zip. zip takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. You won’t be able to see much about this object from just printing it:
```python
names_and_heights = zip(names, heights)
print(names_and_heights)
```
To see the nested lists, you can convert the zip object to a list first:
```python
print(list(names_and_heights))
````
returns
```shell
[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]
```
Example
```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names,dogs_names)
list_of_names_and_dogs = list(names_and_dogs_names)
print(list_of_names_and_dogs)
```
### Growing a List: Plus (+)
When we want to add multiple items to a list, we can use + to combine two lists.

Below, we have a list of items sold at a bakery called items_sold:

```python
items_sold = ['cake', 'cookie', 'bread']
```
Suppose the bakery wants to start selling 'biscuit' and 'tart':
```shell
>>> items_sold_new = items_sold + ['biscuit', 'tart']
>>> print(items_sold_new)
['cake', 'cookie', 'bread', 'biscuit', 'tart']
```
We can only use + with other lists. If we type in this code:
```python
my_list = [1, 2, 3]
my_list + 4
```
we will get the following error:
```shell
TypeError: can only concatenate list (not "int") to list
```
If we want to add a single element using +, we have to put it into a list with brackets ([]):
```python
my_list + [4]
```
Example
```python
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac','iris']


broken_prices = [5, 3, 4, 5, 4] + [4]
```
### Range I
Often, we want to create a list of consecutive numbers. For example, suppose we want a list containing the numbers 0 through 9:
````python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo.

Python gives us an easy way of creating these lists using a function called range. The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:
```python
my_range = range(10)
```
Just like with zip, the range function returns an object that we can convert into a list:
```shell
>>> print(my_range)
range(0, 10)
>>> print(list(my_range))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
### Range II
We can use range to generate more interesting lists.

By default, range creates a list starting at 0. However, if we call range with two arguments, we can create a list that starts at a different number. For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):
```shell
>>> my_list = range(2, 9)
>>> print(list(my_list))
[2, 3, 4, 5, 6, 7, 8]
```
With one or two arguments, range will create a list of consecutive numbers (i.e., each number is one greater than the previous number). If we use a third argument, we can create a list that “skips” numbers. For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:
```shell
>>> my_range2 = range(2, 9, 2)
>>> print(list(my_range2))
[2, 4, 6, 8]
```
We can skip as many numbers as we want! In this example, we’ll start at 1 and skip 10 between each number until we get to 100:
```shell
>>> my_range3 = range(1, 100, 10)
>>> print(list(my_range3))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
```
Exercise
```python
list1 = range(5, 15, 3)
list2 = range(0,40,5)
```

Reviews
```python
first_names = ['Ainsley','Ben','Chani','Depak']
age = []
age.append(42)
all_ages = [32,41,29] + age
name_and_age = zip(first_names, all_ages)
ids = range(4)
```
