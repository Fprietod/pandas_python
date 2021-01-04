menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#A dictionary begins and ends with curly braces ({ and }).
#Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3)
#Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)
#It’s considered good practice to insert a space () after each comma, but your code will still run without the space.
#Dictionaries provide us with a way to map pieces of data to each other, so that we can quickly find values that are associated with one another.
#However, the keys can be numbers as well. For example, if we were mapping restaurant bill subtotals to the bill total after tip
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
#Values can be any type. You can use a string, a number, a list, or even another dictionary as the value associated with a key!
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
#You can also mix and match key and value types. For example:
person = {"name": "Shuri", "age": 18, "siblings": ["T'Chaka", "Ramonda"]}
#Invalid Keys
#We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary
#For example
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#Dictionaries in Python rely on each key having a hash value, a specific identifier for the key.
children = {"von Trapp":["Johannes","Rosmarie","Eleonore"],"Corleone":["Sonny","Fredo","Michael"]}
#Empty dictionary
empty_dict = {}
#Add A Key
#To add a single key : value pair to a dictionary, we can use the syntax:
my_dict["new_key"] = "new_value"
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#I have another way to add values to my dictionary, just create an empty dictionary and add
aimals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['dog'] = 6

animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)

#Add multiples key
#If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
#which would add all three items to the sensors dictionary. Now, sensors looks like:
{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

#Overwrite Values
#n that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
#would yield
{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#List Comprehensions to Dictionaries
#Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
#Python allows you to create a dictionary using a list comprehension, with this syntax:
#sudents = {key:value for key, value in zip(names, heights)}
tudents is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
#Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:
#Takes a pair from the zipped list of pairs from names and heights
#Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
#Creates a key : value item in the students dictionary
#For example, to create a list of pairs between names and heights:
zipped_students = zip(names, heights)
#
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
#Exercise
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)






