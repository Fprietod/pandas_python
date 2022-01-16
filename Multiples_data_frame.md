### Introduction: Multiple DataFrames
In order to efficiently store data, we often spread related information across multiple tables.

For instance, imagine that we own an e-commerce business and we want to track the products that have been ordered from our website.

We could have one table with all of the following information:

order_id
customer_id
customer_name
customer_address
customer_phone_number
product_id
product_description
product_price
quantity
timestamp
However, a lot of this information would be repeated. If the same customer makes multiple orders, that customer’s name, address, and phone number will be reported multiple times. If the same product is ordered by multiple customers, then the product price and description will be repeated. This will make our orders table big and unmanageable.

So instead, we can split our data into three tables:

orders would contain the information necessary to describe an order: order_id, customer_id, product_id, quantity, and timestamp
products would contain the information to describe each product: product_id, product_description and product_price
customers would contain the information for each customer: customer_id, customer_name, customer_address, and customer_phone_number
In this lesson, we will learn the Pandas commands that help us work with data stored in multiple tables.

### Inner Merge II
It is easy to do this kind of matching for one row, but hard to do it for multiple rows.

Luckily, Pandas can efficiently do this for the entire table. We use the .merge() method.

The .merge() method looks for columns that are common between two DataFrames and then looks for rows where those column’s values are the same. It then combines the matching rows into a single row in a new table.

We can call the pd.merge() method with two tables like this:
```python 
new_df = pd.merge(orders, customers)
```
This will match up all of the customer information to the orders that each customer made.

Excersice 
```python 
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)

print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
```
### Inner Merge III
In addition to using pd.merge(), each DataFrame has its own .merge() method. For instance, if you wanted to merge orders with customers, you could use:
```python 
new_df = orders.merge(customers)
```
This produces the same DataFrame as if we had called pd.merge(orders, customers).

We generally use this when we are joining more than two DataFrames together because we can “chain” the commands. The following command would merge orders to customers, and then the resulting DataFrame to products:
```python 
big_df = orders.merge(customers)\
    .merge(products)
```

Excersice 

```python 
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)
men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
```
