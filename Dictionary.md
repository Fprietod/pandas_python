# Introduction dictionary
A dictionary is an unordered set of key: value pairs.

It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

Suppose we want to store the prices of various items sold at a cafe:

   - Avocado Toast is 6 dollars
   - Carrot Juice is 5 dollars
   - Blueberry Muffin is 2 dollars

In Python, we can create a dictionary called menu to store this data:
```python
menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```
Notice that:

  -  A dictionary begins and ends with curly braces { and }.
   - Each item consists of a key ("avocado toast") and a value (6).
   - Each key: value pair is separated by a comma.

It’s considered good practice to insert a space () after each comma, but our code will still run without the space.

## Make a dictionary
In the previous exercise, we saw a dictionary that maps strings to numbers (i.e., "avocado toast": 6). However, the keys can be numbers as well.

For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:

```python
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
```

Values can be of any type. We can use a string, a number, a list, or even another dictionary as the value associated with a key!

For example:
```python
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
```
### Invalid Keys
We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary. If we try to, we will get a TypeError. 

The word “unhashable” in this context means that this ‘list’ is an object that can be changed.

Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.

### Add a key
To add a single key: value pair to a dictionary, we can use the syntax:

dictionary[key] = value

For example, if we had our menu dictionary from the first exercise:

```python
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```
And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:
```python
menu["cheesecake"] = 8
```
Now, menu looks like:

```python
{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}
```
### Add multiple Keys
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:

```python
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
```
If we wanted to add 3 new rooms, we could use:

```python
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
```
This would add all three items to the sensors dictionary.

Now, sensors looks like:

```python
{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}
```
### Overwrite Values
We know that we can add a key by using syntax like:

```python
menu["avocado toast"] = 7

```
This will create a key "avocado toast" and set the value to 7. But what if we already have an 'avocado toast' entry in the menu dictionary?

In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.
```python
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
```

This would yield:
```python
{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```
Notice the value of "oatmeal" has now changed to 5.


### List Comprehensions to Dictionaries
Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:
```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
```
Python allows you to create a dictionary using a list comprehension, with this syntax:
```python
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
```

Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:

    -Takes a pair from the zipped list of pairs from names and heights
   - Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
   - Creates a key : value item in the students dictionary
  -  Repeats steps 1-3 for the entire list of pairs
  
 Example:
 ```python
 drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
```

