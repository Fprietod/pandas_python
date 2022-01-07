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
