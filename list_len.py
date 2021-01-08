toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2,6,1,3,2,7,2]

num_pizzas = len(toppings)

print("we sell " + str(num_pizzas) +" different kinds of pizza!")

pizzas = list(zip(prices,toppings))
print (pizzas)

#sort low to hight
pizzas.sort()
#store the first element
cheapest_pizza = pizzas[0]
#the last element 
priciest_pizza = pizzas[-1]

#lowest cost pizzas
three_cheapest = pizzas[:2]
print(three_cheapest)
#count
num_two_dollar_slices = prices.count(2)
