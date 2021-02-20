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
