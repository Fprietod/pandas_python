# If we want to print some elements of a list its neccesary to use a loop
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print(breed)
  
 #Print a list
 for <temporary variable> in <list variable>:
    <action>
    
 # Print in a range that we need
 promise = "I will not chew gum in class"
for i in range(5):
  print(promise)
 
 # Infinite loops
 
 my_favorite_numbers = [4, 8, 15, 16, 42]
 
for number in my_favorite_numbers:
  my_favorite_numbers.append(1)
 
 
 #What happens here? Every time we enter the loop, we add a 1 to the end of the list that we are iterating through

#Break
#You can stop a for loop from inside the loop by using break. When the program hits a break statement, control returns to the code outside of the for loop. For example:
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]
 
print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")
#This would produce the output:
#Checking the sale list!
#blue_shirt
#striped_socks
#knit_dress
#End of search!

#Example
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
  
# Continue

# Let’s say we want to print out all of the numbers in a list, unless they’re negative. We can use continue to move to the next i in the list:
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
 
for i in big_number_list:
  if i < 0:
    continue
  print(i)
 #This would produce the output:
1
2
4
5
2
#Every time there was a negative number, the continue keyword moved the index to the next value in the list, without executing the code in the rest of the for loop.

#While Loops

#The while loop performs a set of code until some condition is reached.
#While loops can be used to iterate through lists, just like for loops:
dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']


index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1
  #Every time the condition of the while loop (in this case, index < len(dog_breeds)) is satisfied, the code inside the while loop runs. 
  # Excersie
  all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) <6:
  student = all_students.pop() #Take the last item
  students_in_poetry.append(student)
print(students_in_poetry)

#Nested Loops

#Suppose we are in charge of a science class, that is split into three project teams:
#List of sublist, when you have multiple list, its neccesary that you use 2 cycle for each element
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
#If we want to go through each student, we have to put one loop inside another:
for team in project_teams:
  for student in team:
    print(student)
   #The result
  Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel

#Excercise
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
  
print(scoops_sold)
#sales_data loop, go through each location list and add the element to your scoops_sold variable and sum


#List Comprehensions
#We want to make a new list, called usernames, that has all of the strings in words with an '@' as the first character. We know we can do this with a for loop
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []
 
for word in words:
  if word[0] == '@':
    usernames.append(word)

    # Python has a convenient shorthand to create lists like this with one line:
    usernames = [word for word in words if word[0] == '@']
 #This list comprehension:
#Takes an element in words
#Assigns that element to a variable called word
#Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
#Repeats steps 1-3 for all of the strings in words
#Note: if we hadn’t done any checking (let’s say we had omitted if word[0] == '@'), the new list would be just a copy of words:
usernames = [word for word in words]
#usernames is now ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]

#Excercise
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [centimeter for centimeter in heights if centimeter > 161]

print(can_ride_coaster)

#We want to create a new list with the string " please follow me!" added to the end of each username
#We want to call this new list messages. We can use a list comprehension to make this list with one line:
messages = [user + " please follow me!" for user in usernames]
#This list comprehension:

    #Takes a string in usernames
    #Assigns that string to a variable called user
    #Adds “ please follow me!” to user
   # Appends that concatenation to the new list called messages
  #Repeats steps 1-4 for all of the strings in usernames
#Now, messages contains these values:
["@coolguy35 please follow me!", "@kewldawg54 please follow me!", "@matchamom please follow me!"]

#Being able to create lists with modified values is especially useful when working with numbers. Let’s say we have this list:
my_upvotes = [192, 34, 22, 175, 75, 101, 97]
#We want to add 100 to each value. We can accomplish this goal in one line:
updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]

#This list comprehension:

   # Takes a number in my_upvotes
  #  Assigns that number to a variable called vote_value
  #  Adds 100 to vote_value
  #  Appends that sum to the new list updated_upvotes
  #  Repeats steps 1-4 for all of the numbers in my_upvotes

  #Now, updated_upvotes contains these values:
  [292, 134, 122, 275, 175, 201, 197]
  
  # Convert celsius to farenghtfai
  celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [ temperature_in_celsius * 9/5 + 32 for temperature_in_celsius in celsius ]

print(fahrenheit)

#Excercise
