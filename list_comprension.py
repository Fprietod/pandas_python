
nums = [4, 8, 15, 16, 23, 42]
double_nums = [temp * 2 for temp in nums]
quares = [temp **2 for temp in nums]
print(squares)
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]
print(add_ten)
nums = [4, 8, 15, 16, 23, 42]
parity = [num % 2 for num in nums]

#You can get a character of a string by using the syntax [index], where index is the character you want to get, starting at 0.
my_string = "Whoa! A seesaw"
print(my_string[0])
print(my_string[2])
print(my_string[5])
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [nam[0] for nam in names]
print(first_character)
#We can use the not operator to flip the value of a Boolean:
a = False
b = True
 
not_a = not a
not_b = not b
 
print(not_a)
print(not_b)
#Create a new list called is_Jerry, in which an entry at position i is True if the entry in names at position i equals "Jerry". The entry should be False otherwise
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]
print(is_Jerry)
#Create a new list called greater_than_two, in which an entry at position i is True if the entry in nums at position i is greater than 2.
nums = [5, -10, 40, 20, 0]
greater_than_two = [num > 2 for num in nums]
