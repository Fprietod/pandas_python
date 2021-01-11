# If we want to print some elements of a list its neccesary to use a loop
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print(breed)
  
 #Print a list
 for <temporary variable> in <list variable>:
    <action>
    
 # Print in a range that we need
 promise = "I will not chew gum in class"
for i in range(5):
  print(promise)
 
 # Infinite loops
 
 my_favorite_numbers = [4, 8, 15, 16, 42]
 
for number in my_favorite_numbers:
  my_favorite_numbers.append(1)
 
 
 #What happens here? Every time we enter the loop, we add a 1 to the end of the list that we are iterating through
