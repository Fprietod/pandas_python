from matplotlib import pyplot as plt


#Basic Line Plot

#Line graphs are helpful for visualizing how a variable changes over time.

#Some possible data that would be displayed with a line graph:

 #   average prices of gasoline over the past decade
  #  weight of an individual over the past couple of months
   # average temperature along a line of longitude over different latitudes

#Using Matplotlib methods, the following code will create a simple line graph using .plot() and display it using .show() :
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
plt.plot(x_values, y_values)
plt.show()


    # x_values is a variable holding a list of x-values for each point on our line graph
    # y_values is a variable holding a list of y-values for each point on our line graph
    # plt is the name we have given to the Matplotlib module we have imported at the top of the code
    # plt.plot(x_values, y_values) will create the line graph
    # plt.show() will actually display the graph

    
days = [0,1,2,3,4,5,6]
money_spent = [10, 12, 12,10,14,22,24]

plt.plot(days, money_spent)
plt.show()
