### Calculating Column Statistics
Aggregate functions summarize many data points (i.e., a column of a dataframe) into a smaller set of values.

Some examples of this type of calculation include:

The DataFrame customers contains the names and ages of all of your customers. You want to find the median age:
```python 
print(customers.age)
>> [23, 25, 31, 35, 35, 46, 62]
print(customers.age.median())
>> 35
```
The DataFrame shipments contains address information for all shipments that you’ve sent out in the past year. You want to know how many different states you have shipped to (and how many shipments went to the same state).
```python 
print(shipments.state)
>> ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
print(shipments.state.nunique())
>> 3
``` 
The DataFrame inventory contains a list of types of t-shirts that your company makes. You want a list of the colors that your shirts come in.
```python 
print(inventory.color)
>> ['blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'orange', 'orange', 'orange']
print(inventory.color.unique())
>> ['blue', 'green', 'orange']
```
The general syntax for these calculations is:
```python 
df.column_name.command()
```

| Command   | Description                       |
| --------- | --------------------------------- |
| `mean`    | Average of all values in column   |
| `std`     | Standard deviation                |
| `median`  | Median                            |
| `max`     | Maximum value in column           |
| `min`     | Minimum value in column           |
| `count`   | Number of values in column        |
| `nunique` | Number of unique values in column |
| `unique`  | List of unique values in column   |

Our finance department wants to know the price of the most expensive pair of shoes purchased. Save your answer to the variable most_expensive.
```python most_expensive = orders.price.max()
```

Our fashion department wants to know how many different colors of shoes we are selling. Save your answer to the variable num_colors.
```python 
num_colors = orders.shoe_color.nunique()
```
### Calculating Aggregate Functions I
When we have a bunch of data, we often want to calculate aggregate statistics (mean, standard deviation, median, percentiles, etc.) over certain subsets of the data.

Suppose we have a grade book with columns student, assignment_name, and grade. The first few lines look like this:

| student   | assignment\_name | grade |
| --------- | ---------------- | ----- |
| Amy       | Assignment 1     | 75    |
| Amy       | Assignment 2     | 35    |
| Bob       | Assignment 1     | 99    |
| Bob       | Assignment 2     | 35    |
| …<br><br> |

We want to get an average grade for each student across all assignments. We could do some sort of loop, but Pandas gives us a much easier option: the method .groupby.

For this example, we’d use the following command:
```python 
grades = df.groupby('student').grade.mean()
```
In general, we use the following syntax to calculate aggregates:
```python 
df.groupby('column1').column2.measurement()
```
column1 is the column that we want to group by ('student' in our example)
column2 is the column that we want to perform a measurement on (grade in our example)
measurement is the measurement function we want to apply (mean in our example)

### Calculating Aggregate Functions II
After using groupby, we often need to clean our resulting data.

As we saw in the previous exercise, the groupby function creates a new Series, not a DataFrame. For our ShoeFly.com example, the indices of the Series were different values of shoe_type, and the name property was price.

Usually, we’d prefer that those indices were actually a column. In order to get that, we can use reset_index(). This will transform our Series into a DataFrame and move the indices into their own column.

Generally, you’ll always see a groupby statement followed by reset_index:
```python 
df.groupby('column1').column2.measurement()
    .reset_index()
```
When we use groupby, we often want to rename the column we get as a result. For example, suppose we have a DataFrame teas containing data on types of tea:
| id | tea               | category | caffeine | price |
| -- | ----------------- | -------- | -------- | ----- |
| 0  | earl grey         | black    | 38       | 3     |
| 1  | english breakfast | black    | 41       | 3     |
| 2  | irish breakfast   | black    | 37       | 2.5   |
| 3  | jasmine           | green    | 23       | 4.5   |
| 4  | matcha            | green    | 48       | 5     |
| 5  | camomile          | herbal   | 0        | 3     |

We want to find the number of each category of tea we sell. We can use:

```python
teas_counts = teas.groupby('category').id.count().reset_index()
```
| category  | id     |
| --------- | ------ |
| 0         | black  | 3 |
| 1         | green  | 4 |
| 2         | herbal | 8 |
| 3         | white  | 2 |
| …<br><br> |

The new column contains the counts of each category of tea sold. We have 3 black teas, 4 green teas, and so on. However, this column is called id because we used the id column of teas to calculate the counts. We actually want to call this column counts. Remember that we can rename columns:
```python 
teas_counts = teas_counts.rename(columns={"id": "counts"})
``` 
| category  | counts |
| --------- | ------ |
| 0         | black  | 3 |
| 1         | green  | 4 |
| 2         | herbal | 8 |
| 3         | white  | 2 |
| …<br><br> |

Excercise 
```python 
orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))
```
### Calculating Aggregate Functions III
Sometimes, the operation that you want to perform is more complicated than mean or count. In those cases, you can use the apply method and lambda functions, just like we did for individual column operations. Note that the input to our lambda function will always be a list of values.

A great example of this is calculating percentiles. Suppose we have a DataFrame of employee information called df that has the following columns:

id: the employee’s id number
name: the employee’s name
wage: the employee’s hourly wage
category: the type of work that the employee does

| id        | name          | wage | category  |
| --------- | ------------- | ---- | --------- |
| 10131     | Sarah Carney  | 39   | product   |
| 14189     | Heather Carey | 17   | design    |
| 15004     | Gary Mercado  | 33   | marketing |
| 11204     | Cora Copaz    | 27   | design    |
| …<br><br> |

If we want to calculate the 75th percentile (i.e., the point at which 75% of employees have a lower wage and 25% have a higher wage) for each category, we can use the following combination of apply and a lambda function:
```python 
# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()
```
The output will be 
| category  | wage      |
| --------- | --------- |
| 0         | design    | 23 |
| 1         | marketing | 35 |
| 2         | product   | 48 |
| …<br><br> |

Excercise 
Once more, we’ll return to the data from ShoeFly.com. Our Marketing team says that it’s important to have some affordably priced shoes available for every color of shoe that we sell.

Let’s calculate the 25th percentile for shoe price for each shoe_color to help Marketing decide if we have enough cheap shoes on sale. Save the data to the variable cheap_shoes.

Note: Be sure to use reset_index() at the end of your query so that cheap_shoes is a DataFrame.
```python 
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()
print(cheap_shoes)
``` 

Calculating Aggregate Functions IV
Sometimes, we want to group by more than one column. We can easily do this by passing a list of column names into the groupby method.

Imagine that we run a chain of stores and have data about the number of sales at different locations on different days:

| Location     | Date       | Day of Week | Total Sales |
| ------------ | ---------- | ----------- | ----------- |
| West Village | February 1 | W           | 400         |
| West Village | February 2 | Th          | 450         |
| Chelsea      | February 1 | W           | 375         |
| Chelsea      | February 2 | Th          |


We suspect that sales are different at different locations on different days of the week. In order to test this hypothesis, we could calculate the average sales for each store on each day of the week across multiple months. The code would look like this:
```python 
df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
```
The results might look something like this:
| Location     | Day of Week | Total Sales |
| ------------ | ----------- | ----------- |
| Chelsea      | M           | 402.50      |
| Chelsea      | Tu          | 422.75      |
| Chelsea      | W           | 452.00      |
| …            |             |             |
| West Village | M           | 390         |
| West Village | Tu          | 400         |
| …<br><br>    |

Excersise 

At ShoeFly.com, our Purchasing team thinks that certain shoe_type/shoe_color combinations are particularly popular this year (for example, blue ballet flats are all the rage in Paris).

Create a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased. Save it to the variable shoe_counts.

You should be able to do this using groupby and count().

Note: When we’re using count(), it doesn’t really matter which column we perform the calculation on. You should use id in this example, but we would get the same answer if we used shoe_type or last_name.

Remember to use reset_index() at the end of your code!
```python 
orders = pd.read_csv('orders.csv')
shoe_counts = orders.groupby(['shoe_type','shoe_color']).id.count().reset_index()
print(shoe_counts)
```

### Pivot Tables
When we perform a groupby across multiple columns, we often want to change how our data is stored. For instance, recall the example where we are running a chain of stores and have data about the number of sales at different locations on different days:

| Location     | Date       | Day of Week | Total Sales |
| ------------ | ---------- | ----------- | ----------- |
| West Village | February 1 | W           | 400         |
| West Village | February 2 | Th          | 450         |
| Chelsea      | February 1 | W           | 375         |
| Chelsea      | February 2 | Th          |

We suspected that there might be different sales on different days of the week at different stores, so we performed a groupby across two different columns (Location and Day of Week). This gave us results that looked like this:

| Location     | Day of Week | Total Sales |
| ------------ | ----------- | ----------- |
| Chelsea      | M           | 300         |
| Chelsea      | Tu          | 310         |
| Chelsea      | W           | 320         |
| Chelsea      | Th          | 290         |
| …            |             |             |
| West Village | Th          | 400         |
| West Village | F           | 390         |
| West Village | Sa          | 250         |

In order to test our hypothesis, it would be more useful if the table was formatted like this:

| Location     | M   | Tu  | W   | Th  | F   | Sa  | Su  |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
| Chelsea      | 400 | 390 | 250 | 275 | 300 | 150 | 175 |
| West Village | 300 | 310 | 350 | 400 | 390 | 250 | 200 |
| …            |     |     |     |     |     |     |

Reorganizing a table in this way is called pivoting. The new table is called a pivot table.

In Pandas, the command for pivot is:

```python 
df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
 ```
 
 Example:
 
 ```python 
 # First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')
  ```
  Just like with groupby, the output of a pivot command is a new DataFrame, but the indexing tends to be “weird”, so we usually follow up with .reset_index().
  
  Excercise 
  
  In the previous example, you created a DataFrame with the total number of shoes of each shoe_type/shoe_color combination purchased for ShoeFly.com.

The purchasing manager complains that this DataFrame is confusing.

Make it easier for her to compare purchases of different shoe colors of the same shoe type by creating a pivot table. Save your results to the variable shoe_counts_pivot.

Your table should look like this:
```python 
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
  columns = 'shoe_color',
  index = 'shoe_type',
  values = 'id'
).reset_index()
print(shoe_counts)
print(shoe_counts_pivot)
```

  

