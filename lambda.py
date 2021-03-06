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
#Multiple
multiple_of_three = lambda num: "multiple of three" if num %3 ==0 else 'not a multiple'
# Comparisons can be done using:

  #  <: less than
   # <=: less than or equal to
   # >: greater than
   # >=: greater than or equal to
   # ==: equal to
   # !=: not equal to
  
  rate_movie = lambda rating: 'I liked this movie' if rating > 8.5 else 'This movie was not very good'
  #You can use the modulo function (%) with 10 to find the ones’ place of an integer.
  #Double square
  #or by using the exponential operator **:
  
  #Add Random

#random.randint(a,b) will return an integer between a and b (inclusive).

#So, random.randint(5, 8) could return any integer between 5 and 8 including both 5 and 8.

#random.randint(0, 100) could return any integer between 0 and 100 including both 0 and 100.
add_random = lambda num: num + random.randint(1,10)

#Open a file
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)

#This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. Then we print cool_contents, which outputs the statement Wowsers!.
# But what if we wanted to store each line in a variable? We can use the .readlines() 
#function to read a text file line by line instead of having the whole thing
with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)
    #The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt. It then iterates over each line in the document and prints the entire file out.
    
    #Reading Line
    #Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(), which will only read a single line at a time.
    with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)
  #It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line
  #It then saves the second line (So make the most of this, your little day,) into the variable second_line and then prints it out. 
  #Write file
  with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
  #Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. 
  #The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.
  #This code creates a new file in the same folder as script.py and gives it the text What an incredible file!
  #Appending to a File
  #Of course there is! Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode.
  #Then we can add another line to that file with the following code:
  with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("... and it still is")
  #Notice that opening the file in append-mode, with 'a' as an argument to open(), means that using the file object’s .write() method appends whatever is passed to the end of the file in a new line
  # In Python we can convert that data into a dictionary using the csv library’s DictReader object. Read CSV
  import csv
 
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
# We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV. 
#We pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV 
#After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries which we can use access methods for.
#The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.
#When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). 
#By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.
import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])
   
  #Reading different type of cv
  #Notice the \n character, this is the escape sequence for a new line.
  #The possibility of a new line escaped by a \n character in our data is why we pass the newline='' keyword argument to the open() function.
  import csv
 
with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
    
   #Exercise create a list and get the ID number of every book
   with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN']for book in books_reader]
  #Writing a CSV FILE
  #First import the csv module
  import csv
  big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]
  
  with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
 
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
    
  #In our code above we had a set of dictionaries with the same keys for each, a prime candidate for a CSV. We import the csv library, and then open a new CSV file in write-mode by passing the 'w' argument to the open() function. 
  #  We then instantiate our CSV writer object and pass two arguments. The first is output_csv, the file handler object. The second is our list of fields fields which we pass to the keyword parameter fieldnames.
#First we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file.
#Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as the keys.
#Reading a JSON File
import json
 
with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])

#We continue by parsing purchase_json using json.load(), creating a Python dictionary out of the file. Saving the results into purchase_data means we can interact with it
# WRITE JSON OBJECT
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}
import json
 
with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
  #We import the json module, open up a write-mode file under the variable json_file, and then use the json.dump() method to write to the file. 
  #json.dump() takes two arguments: first the data object, then the file object you want to save.

