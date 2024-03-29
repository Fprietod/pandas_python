Our favorite online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.

1.
Examine the first few rows of ad_clicks.

2.
Your manager wants to know which ad platform is getting you the most views.

How many views (i.e., rows of the table) came from each utm_source?

3.
If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.

4.
We want to know the percent of people who clicked on ads from each utm_source.

Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.

5.
Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

Save your results to the variable clicks_pivot.


6. Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

Was there a difference in click rates for each source?

7.
The column experimental_group tells us whether the user was shown Ad A or Ad B.

Were approximately the same number of people shown both ads?


8.
Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

9.
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.


10.
For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.

```python 
ad_clicks = pd.read_csv('ad_clicks.csv')
# Parte 1
print(ad_clicks.head(5))
#Parte 2
source=ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(source)
# Parte 3 
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
# Parte 4
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

print (clicks_by_source)
# Parte 5
clicks_pivot = clicks_by_source.pivot(
  index = 'utm_source',
  columns = 'is_click',
  values = 'user_id'
).reset_index()
print(clicks_pivot)
# Parte 6 
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])
# Parte 7 
print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())
# Parte 8 
print(ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot (
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
).reset_index())

# Parte 9 
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
# Parte 10 
a_clicks_pivot = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()
a_clicks_pivot['percent_clicked']= a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)
```
