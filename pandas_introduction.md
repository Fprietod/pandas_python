# Create a Data Frame I 
~~~
A DataFrame is an object that stores data as rows and columns. You can think of a DataFrame as a spreadsheet or as a SQL table. You can manually create a DataFrame or fill it with data from a CSV, an Excel spreadsheet, or a SQL query.

DataFrames have rows and columns. Each column has a name, which is a string. Each row has an index, which is an integer. DataFrames can contain many different data types: strings, ints, floats, tuples, etc.

You can pass in a dictionary to pd.DataFrame(). Each key is a column name and each value is a list of column values. The columns must all be the same length or you will get an error. Here’s an example:
~~~
```python
df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})

```
## Create a Data Frame II
You can also add data using lists.

For example, you can pass in a list of lists, where each one represents a row of data. Use the keyword argument columns to pass a list of column names. 
```python
df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])
```
 
### Comma Separated Variables (CSV)
~~~
We now know how to create our own DataFrame. However, most of the time, we’ll be working with datasets that already exist. One of the most common formats for big datasets is the CSV.

CSV (comma separated values) is a text-only spreadsheet format. You can find CSVs in lots of places:

    Online datasets (here’s an example from data.gov)
    Export from Excel or Google Sheets
    Export from SQL

The first row of a CSV contains column headings. All subsequent rows contain values. Each column heading and each variable is separated by a comma:
~~~
### Loading and Saving CSVs
When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():
```python
pd.read_csv('my-csv-file.csv')
```
In the example above, the .read_csv() method is called. The CSV file called my-csv-file is passed in as an argument.

We can also save data to a CSV, using .to_csv().
```python
df.to_csv('new-csv-file.csv')
```
In the example above, the .to_csv() method is called on df (which represents a DataFrame object). The name of the CSV file is passed in as an argument (new-csv-file.csv). By default, this method will save the CSV file in your current directory.

### Inspect a Data Frame
~~~
When we load a new DataFrame from a CSV, we want to know what it looks like.

If it’s a small DataFrame, you can display it by typing print(df).

If it’s a larger DataFrame, it’s helpful to be able to inspect a few items without having to look at the entire DataFrame.

The method .head() gives the first 5 rows of a DataFrame. If you want to see more rows, you can pass in the positional argument n. For example, df.head(10) would show the first 10 rows.

The method df.info() gives some statistics for each column.
~~~
### Select Columns
~~~
Now we know how to create and load data. Let’s select parts of those datasets that are interesting or important to our analyses.

Suppose you have the DataFrame called customers, which contains the ages of your customers: 

Perhaps you want to take the average or plot a histogram of the ages. In order to do either of these tasks, you’d need to select the column.

There are two possible syntaxes for selecting all values from a column:
~~~
- Select the column as if you were selecting a value from a dictionary using a key. In our example, we would type customers['age'] to select the ages.
-  If the name of a column follows all of the rules for a variable name (doesn’t start with a number, doesn’t contain spaces or special characters, etc.), then you          can select it using the following notation: df.MySecondColumn. In our example, we would type customers.age.

When we select a single column, the result is called a Series.
```python
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
        
)
´´´python
clinic_north = df['clinic_north']
print(type(clinic_north))
print(type(df))
```
### Selecting multiple columns
When you have a larger DataFrame, you might want to select just a few columns.

For instance, let’s return to a DataFrame of orders from ShoeFly.com:
~~~

id 	first_name 	last_name 	email 	shoe_type 	shoe_material 	shoe_color
54791 	Rebecca 	Lindsay 	RebeccaLindsay57@hotmail.com 	clogs 	faux-leather 	black
53450 	Emily 	Joyce 	EmilyJoyce25@gmail.com 	ballet flats 	faux-leather 	navy
91987 	Joyce 	Waller 	Joyce.Waller@gmail.com 	sandals 	fabric 	black
14437 	Justin 	Erickson 	Justin.Erickson@outlook.com 	clogs 	faux-leather 	red
~~~
We might just be interested in the customer’s last_name and email. We want a DataFrame like this:
~~~
last_name 	email
Lindsay 	RebeccaLindsay57@hotmail.com
Joyce 	EmilyJoyce25@gmail.com
Waller 	Joyce.Waller@gmail.com
Erickson 	Justin.Erickson@outlook.com
~~~

To select two or more columns from a DataFrame, we use a list of the column names. To create the DataFrame shown above, we would use:
```python
new_df = orders[['last_name', 'email']]
```
Note: *Make sure that you have a double set of brackets ([[]]), or this command won’t work!
```python
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north_south = df[['clinic_north','clinic_south']]
print(type(clinic_north_south))
```
### Select Rows
Let’s revisit our orders from ShoeFly.com:
~~~
 id 	first_name 	last_name 	email 	shoe_type 	shoe_material 	shoe_color
54791 	Rebecca 	Lindsay 	RebeccaLindsay57@hotmail.com 	clogs 	faux-leather 	black
53450 	Emily 	James 	EmilyJames25@gmail.com 	ballet flats 	faux-leather 	navy
91987 	Joyce 	Waller 	Joyce.Waller@gmail.com 	sandals 	fabric 	black
14437 	Justin 	Erickson 	Justin.Erickson@outlook.
~~~
~~~
Maybe our Customer Service department has just received a message from Joyce Waller, so we want to know exactly what she ordered. We want to select this single row of data.

DataFrames are zero-indexed, meaning that we start with the 0th row and count up from there. Joyce Waller’s order is the 2nd row.
~~~
We select it using the following command:
```python
orders.iloc[2]
```
```python
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
march =df.iloc[2]
```
### Selecting multiple columns
You can also select multiple rows from a DataFrame.
~~~
 id 	first_name 	last_name 	email 	shoe_type 	shoe_material 	shoe_color
54791 	Rebecca 	Lindsay 	RebeccaLindsay57@hotmail.com 	clogs 	faux-leather 	black
53450 	Emily 	James 	EmilyJames25@gmail.com 	ballet flats 	faux-leather 	navy
91987 	Joyce 	Waller 	Joyce.Waller@gmail.com 	sandals 	fabric 	black
14437 	Justin 	Erickson 	Justin.Erickson@outlook.
~~~
Here are some different ways of selecting multiple rows: 
- orders.iloc[3:7] would select all rows starting at the 3rd row and up to but not including the 7th row (i.e., the 3rd row, 4th row, 5th row, and 6th row) 
- orders.iloc[:4] would select all rows up to, but not including the 4th row (i.e., the 0th, 1st, 2nd, and 3rd rows) 
- orders.iloc[-3:] would select the rows starting at the 3rd to last row and up to and including the final row 
```python
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
april_may_june = df[-3:]
print(april_may_june)
```
### Select rows with logic I
You can select a subset of a DataFrame by using logical statements:
```python
df[df.MyColumnName == desired_column_value]
```
We have a large DataFrame with information about our customers. A few of the many rows look like this:
~~~
name 	address 	phone 	age
Martha Jones 	123 Main St. 	234-567-8910 	28
Rose Tyler 	456 Maple Ave. 	212-867-5309 	22
Donna Noble 	789 Broadway 	949-123-4567 	35
Amy Pond 	98 West End Ave. 	646-555-1234 	29
~~~
Suppose we want to select all rows where the customer’s age is 30. We would use:
```python
df[df.age == 30]
```
In Python, == is how we test if a value is exactly equal to another value.

We can use other logical statements, such as:
- Greater Than, > — Here, we select all rows where the customer’s age is greater than 30:
```python
df[df.age > 30]
```
- Less Than, < — Here, we select all rows where the customer’s age is less than 30:
```python
df[df.age < 30]
```
Not Equal, != — This snippet selects all rows where the customer’s name is not Clara Oswald:
```python
df[df.name != 'Clara Oswald']
```
Example:
```python

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
january = df[df.month == 'January']
print(january)
```

### Select rows with logic II

You can also combine multiple logical statements, as long as each statement is in parentheses.

For instance, suppose we wanted to select all rows where the customer’s age was under 30 or the customer’s name was “Martha Jones”:

|name|	|address|	|phone|	|age|
|Martha Jones	123 Main St.	234-567-8910	28|
|Rose Tyler	456 Maple Ave.	212-867-5309	22|
|Donna Noble	789 Broadway	949-123-4567	35|
|Amy Pond	98 West End Ave.	646-555-1234	29|
|Clara Oswald	54 Columbus Ave.	714-225-1957	31|
…		


```python 

df[(df.age < 30) |
   (df.name == 'Martha Jones')]
   
   march_april = df[(df.month == 'March')| (df.month == 'April')]

print(march_april)
```
In Python, | means “or” and & means “and”.

### Select rows with logic III

Suppose we want to select the rows where the customer’s name is either “Martha Jones”, “Rose Tyler” or “Amy Pond”.

We could use the isin command to check that df.name is one of a list of values:
```python
df[df.name.isin(['Martha Jones',
     'Rose Tyler',
     'Amy Pond'])]
# Excersise

january_february_march = df[df.month.isin(['January','February','March'])]

print(january_february_march)

```

### Setting indices

When we select a subset of a DataFrame using logic, we end up with non-consecutive indices. This is inelegant and makes it hard to use .iloc().

We can fix this using the method .reset_index(). For example, here is a DataFrame called df with non-consecutive indices:

| First Name   | Last Name  |   
|---|---|---|---|---| ---------|
| 0	John	|Smith
|4	Jane|	|Doe|
|7	Joe	Schmo  |          |   

If we use the command 
```python 
df.reset_index()
``` 
we get a new DataFrame with a new set of indices:
Note that the old indices have been moved into a new column called 'index'. Unless you need those values for something special, it’s probably better to use the keyword drop=True so that you don’t end up with that extra column. If we run the command df.reset_index(drop=True), we get a new DataFrame that looks like this:
Using
```python
reset_index() 
```
will return a new DataFrame, but we usually just want to modify our existing DataFrame. If we use the keyword inplace=True we can just modify our existing DataFrame.

#Excercise 

Review
You’ve completed the lesson! You’ve just learned the basics of working with a single table in Pandas, including:

Create a table from scratch
Loading data from another file
Selecting certain rows or columns of a table
Let’s practice what you’ve learned.

1. In this example, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store. You’ve seen this data; now it’s your turn to work with it!

Load the data from shoefly.csv into the variable orders.

2.Inspect the first 5 lines of the data.

3.Your marketing department wants to send out an email blast to everyone who ordered shoes!

Select all of the email addresses from the column email and save them to a variable called emails.

4.
Frances Palmer claims that her order was wrong. What did Frances Palmer order?

Use logic to select that row of orders and save it to the variable frances_palmer.


5.
We need some customer reviews for our comfortable shoes. Select all orders for shoe_type: clogs, boots, and ballet flats and save them to the variable comfy_shoes.

```python

#Part 1: reading the csv
orders = pd.read_csv('shoefly.csv')

#Part 2: inspecting the first five lines of data
print(orders.head(5))

#Part 3: selecting the column 'email'
emails = orders.email

#Part 4: the Frances Palmer incident
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

#Part 5: Comfy feet means more time on the street
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
```
## Modifying DataFrames

In the previous lesson, you learned what a DataFrame is and how to select subsets of data from one.

In this lesson, you’ll learn how to modify an existing DataFrame. Some of the skills you’ll learn include:

Adding columns to a DataFrame
Using lambda functions to calculate complex quantities
Renaming columns

### Adding a Column I

Sometimes, we want to add a column to an existing DataFrame. We might want to add new information or perform a calculation based on the data that we already have.

One way that we can add a new column is by giving a list of the same length as the existing DataFrame.

Suppose we own a hardware store called The Handy Woman and have a DataFrame containing inventory information:
It looks like the actual quantity of each product in our warehouse is missing!

Let’s use the following code to add that information to our DataFrame.
```python
df['Quantity'] = [100, 150, 50, 35]
```

Excercise 
```python
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes','Yes','No','No']

```
### Adding a Column II
We can also add a new column that is the same for all rows in the DataFrame
Suppose we know that all of our products are currently in-stock. We can add a column that says this:
```python
df['In Stock?'] = True
```

###Adding a Column III
Finally, you can add a new column by performing a function on the existing columns.

Maybe we want to add a column to our inventory table with the amount of sales tax that we need to charge for each item. The following code multiplies each Price by 0.075, the sales tax for our state:
```python
df['Sales Tax'] = df.Price * 0.075
```
Excerise add the diference 
```python 
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add column here
df['Margin'] = df.Price - df['Cost to Manufacture']
print(df)
```
## Performing Column Operations

It’s a little annoying that the capitalization is different for each row. Perhaps we’d like to make it more consistent by making all of the letters uppercase.

We can use the apply function to apply a function to every value in a particular column. For example, this code overwrites the existing 'Name' columns by applying the function upper to every row in 'Name'.

```python
df['Name'] = df.Name.apply(str.upper)
```
Exercise 
```python 
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name']= df.Name.apply(str.lower)

print(df)
```
##Reviewing Lambda Function
A lambda function is a way of defining a function in a single line of code. Usually, we would assign them to a variable.

For example, the following lambda function multiplies a number by 2 and then adds 3:
```python
mylambda = lambda x: (x * 2) + 3
print(mylambda(5))
```

Lambda functions work with all types of variables, not just integers! Here is an example that takes in a string, assigns it to the temporary variable x, and then converts it into lowercase:
```python
stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))
```

Create a lambda function mylambda that returns the first and last letters of a string, assuming the string is at least 2 characters long. For example,
```python 
mylambda = lambda x: x[0]+x[-1]
print(mylambda('Hello World'))
```

##Reviewing Lambda Function: If Statements
We can make our lambdas more complex by using a modified form of an if statement.

Suppose we want to pay workers time-and-a-half for overtime (any work above 40 hours per week). The following function will convert the number of hours into time-and-a-half hours using an if statement:

```python
def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
 ```
 Below is a lambda function that does the same thing:

 ```python
myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
```
In general, the syntax for an if function in a lambda function is:
```python
lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]
``` 
Exercise 

You are managing the webpage of a somewhat violent video game and you want to check that each user’s age is 13 or greater when they visit the site.

Write a lambda function that takes an inputted age and either returns Welcome to BattleCity! if the user is 13 or older or You must be over 13 if they are younger than 13. Your lambda function should be called mylambda.

```python 
mylambda = lambda x: 'Welcome to BattleCity!' if x>= 13 else "You must be over 13"
print(mylambda(13))
```

## Applying a Lambda to a Column
In Pandas, we often use lambda functions to perform complex operations on columns. For example, suppose that we want to create a column containing the email provider for each email address in the following table:

We could use the following code with a lambda function and the string method .split():
```python 
df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1]
    )
 ```
 Exercise 
 
 Create a lambda function get_last_name which takes a string with someone’s first and last name (i.e., John Smith), and returns just the last name (i.e., Smith).
 The DataFrame df represents the hours worked by different employees over the course of the week. It contains the following columns:

'name': The employee’s name
'hourly_wage': The employee’s hourly wage
'hours_worked': The number of hours worked this week
Use the lambda function get_last_name to create a new column last_name with only the employees’ last name.

```python
import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)
```
### Applying a Lambda to a Row
We can also operate on multiple columns at once. If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, not a column. To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].

If we want to add in the price with tax for each line, we’ll need to look at two columns: Price and Is taxed?.

If Is taxed? is Yes, then we’ll want to multiply Price by 1.075 (for 7.5% sales tax).

If Is taxed? is No, we’ll just have Price without multiplying it.

We can create this column using a lambda function and the keyword axis=1:
```python 
df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.075
     if row['Is taxed?'] == 'Yes'
     else row['Price'],
     axis=1
)
```
Excercise 
If an employee worked for more than 40 hours, she needs to be paid overtime (1.5 times the normal hourly wage).

For instance, if an employee worked for 43 hours and made $10/hour, she would receive $400 for the first 40 hours that she worked, and an additional $45 for the 3 hours of overtime, for a total for $445.

Create a lambda function total_earned that accepts an input row with keys hours_worked and hourly_wage and uses an if statement to calculate the hourly wage.
```python 
df = pd.read_csv('employees.csv')
print (df)
 
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5)* (row.hours_worked - 40))  \
if row.hours_worked > 40 \
else row.hourly_wage * row.hours_worked 
df['total_earned'] = df.apply(total_earned, axis = 1)
print(df)
```
## Renaming Columns

When we get our data from other sources, we often want to change the column names. For example, we might want all of the column names to follow variable name rules, so that we can use df.column_name (which tab-completes) rather than df['column_name'] (which takes up extra space).

You can change all of the column names at once by setting the .columns property to a different list. This is great when you need to change all of the column names at once, but be careful! You can easily mislabel columns if you get the ordering wrong. Here’s an example:
```python 
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']
```
### Renaming Columns II
You also can rename individual columns by using the .rename method. Pass a dictionary like the one below to the columns keyword argument:
```bash 
{'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'}
```
This is the code 
```python 
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
```

The code above will rename name to First Name and age to Age.

Using rename with only the columns keyword will create a new DataFrame, leaving your original DataFrame unchanged. That’s why we also passed in the keyword argument inplace=True. Using inplace=True lets us edit the original DataFrame.

There are several reasons why .rename is preferable to .columns:

You can rename just one column
You can be specific about which column names are getting changed (with .column you can accidentally switch column names if you’re not careful)
Note: If you misspell one of the original column names, this command won’t fail. It just won’t change anything.

If we didn’t know that df was a table of movie ratings, the column name might be confusing.

To clarify, let’s rename name to movie_title.

Use the keyword inplace=True so that you modify df rather than creating a new DataFrame!

```python 
df = pd.read_csv('imdb.csv')

df.rename(columns = {'name': 'movie_title'}, inplace = True)

print(df)
```

Excercise 
1 Parte Once more, you’ll be the data analyst for ShoeFly.com, a fictional online shoe store.

More messy order data has been loaded into the variable orders. Examine the first 5 rows of the data using print and head.


2. Many of our customers want to buy vegan shoes (shoes made from materials that do not come from animals). Add a new column called shoe_source, which is vegan if the materials is not leather and animal otherwise.

Our marketing department wants to send out an email to each customer. Using the columns last_name and gender create a column called salutation which contains Dear Mr. <last_name> for men and Dear Ms. <last_name> for women.

Code 
```python
orders = pd.read_csv('shoefly.csv')
# 1 parte
print(orders.head(5))
# 2 parte
orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')
# 3 parte
orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)





