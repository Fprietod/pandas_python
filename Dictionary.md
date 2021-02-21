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

## Get A Key
Once you have a dictionary, you can access the values in it by providing the key. For example, let’s imagine we have a dictionary that maps buildings to their heights, in meters:
```python
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
```
Then we can access the data in it like this:
```shell
>>> building_heights["Burj Khalifa"]
828
>>> building_heights["Ping An"]
599
```
### Get an Invalid Key
One way to avoid this error is to first check if the key exists in the dictionary:
```python
key_to_check = "Landmark 81"
 
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
  ```
### Try/Except to Get a Key
We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except:
```python
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")
  ```
When we try to access a key that doesn’t exist, the program will go into the except block and print "That key doesn't exist!".
```python
caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")
  ```
### Safely Get a Key
Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:
```python
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
 
#this line will return 632:
building_heights.get("Shanghai Tower")
 
#this line will return None:
building_heights.get("My House")
```
You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:
```shell
>>> building_heights.get('Shanghai Tower', 0)
632
>>> building_heights.get('Mt Olympus', 0)
0
>>> building_heights.get('Kilimanjaro', 'No Value')
'No Value'
```
Example
```python
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder",100000)
print (tc_id)

stack_id = user_ids.get("superStackSmash",100000)
```
### Delete a Key
Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:
```python
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
```

When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize has been given away. We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:
```python
>>> raffle.pop(320291, "No Prize")
"Gift Basket"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(100000, "No Prize")
"No Prize"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(872921, "No Prize")
"Concert Tickets"
>>> raffle
{223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
```
.pop() works to delete items from a dictionary, when you know the key value.
```python
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
```

