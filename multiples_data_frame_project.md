Page Visits Funnel
Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

In this case, our funnel is going to describe the following process:

A user visits CoolTShirts.com
A user adds a t-shirt to their cart
A user clicks “checkout”
A user actually purchases a t-shirt

Funnel for Cool T-Shirts Inc.


1.
Inspect the DataFrames using print and head:

visits lists all of the users who have visited the website
cart lists all of the users who have added a t-shirt to their cart
checkout lists all of the users who have started the checkout
purchase lists all of the users who have purchased a t-shirt

2.
Combine visits and cart using a left merge.

Hint

If we want to combine df1 and df2 with a left merge, we use the following code:

pd.merge(df1, df2, how='left')
OR

df1.merge(df2, how='left')

3.
How long is your merged DataFrame?

Hint

Use len to find out the number of rows in a DataFrame.

4.
How many of the timestamps are null for the column cart_time?

What do these null rows mean?

Hint

You can select null rows from column1 of a DataFrame df using the following code:

df[df.column1.isnull()]

5.
What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?

Note: To calculate percentages, it will be helpful to turn either the numerator or the denominator into a float, by using float(), with the number to convert passed in as input. Otherwise, Python will use integer division, which truncates decimal points.

Hint

If a row of your merged DataFrame has cart_time equal to null, then that user visited the website, but did not place a t-shirt in their cart.

6.
Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?

Stuck? Get a hint


7.
Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.

Examine the result using print and head.

Stuck? Get a hint


8.
What percentage of users proceeded to checkout, but did not purchase a t-shirt?

9.
Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

How might Cool T-Shirts Inc. change their website to fix this problem?
Average Time to Purchase


10.
Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.

Stuck? Get a hint


11.
Examine the results by printing the new column to the screen.

Stuck? Get a hint


12.
Calculate the average time to purchase by applying the .mean() function to your new column.

Video that resolve this --> https://www.youtube.com/watch?v=WKwG14ozDk4
