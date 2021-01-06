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

#Get A Key
#Once you have a dictionary, you can access the values in it by providing the key
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
>>> building_heights["Burj Khalifa"]
#Check if the key be in the dictionary
key_to_check = "Landmark 81"
 
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
 #Try/Except to Get a Key
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")
  
 #Example
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30
#Safely Get a Key

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffein Level")
  
 #Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using.
 #If the key you are trying to .get() does not exist, it will return None by default:
  #Example
  building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
 
#this line will return 632:
building_heights.get("Shanghai Tower")
 
#this line will return None:
building_heights.get("My House")

#You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:
>>> building_heights.get('Shanghai Tower', 0)
632
>>> building_heights.get('Mt Olympus', 0)
0
>>> building_heights.get('Kilimanjaro', 'No Value')
'No Value'
###########################################
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder', 100000) #"teracoder,10000" if the value dont exist
print(tc_id)

stack_id = user_ids.get('superStackSmash',100000)
print(stack_id)
#Delete Key
#the prize and also remove that pair from the dictionary, since the prize has been given away. We can use .pop() to do this. Just like with .get(), 
#we can provide a default value to return if the key does not exist in the dictionary:
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
###################
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
#.pop() works to delete items from a dictionary, when you know the key value.
#Excersice
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains",0)
health_points += available_items.pop("power stew",0)
health_points += available_items.pop("mystic bread",0)

print(available_items)
print(health_points)
##########################################
#Get All Keys
#Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:
>>> list(test_scores)
["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
#Dictionaries also have a .keys() method that returns a dict_keys object. A dict_keys object is a view object, which provides a look at the current state of the dictionary
#The dict_keys object returned by .keys() is a set of the keys in the dictionary. You cannot add or remove elements from a dict_keys object
# A dict_keys object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything.
for student in test_scores.keys():
  print(student)
 
#Get All Values
#Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!)
# with all of the values in the dictionary. 
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
 
for score_list in test_scores.values():
  print(score_list)
#There is no built-in function to get all of the values as a list, but if you really want to, you can use:
list(test_scores.values())
#excersise
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)

#Get all items
#You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list
# Each element of the dict_list returned by .items() is a tuple consisting of:
#(key, value)
#You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list object.
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
 
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
  
  
  #Apple has a value of 184 billion dollars.
#Google has a value of 141.7 billion dollars.
#Microsoft has a value of 80 billion dollars.
#Coca-Cola has a value of 69.7 billion

#Example
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
  
 #Example
 new_dict["new key"] = old_dict.pop("old key")
 for key, value in spread.items():
  print("Your "+key+" is the "+value+" card. ")
  







