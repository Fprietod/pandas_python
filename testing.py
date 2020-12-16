from scipy.stats import chi2_contingency

# Record Data from Google Analytics
control_group = 7700
variant_group = 7700
control_success = 231
variant_success = 308
control_fail = control_group - control_success
variant_fail = variant_group - variant_success

# Perform Chi2 Test
results = chi2_contingency([
  [control_fail, control_success],
  [variant_fail, variant_success]
])

p = results[1]

# Paste Code Here:
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)
# LIST
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64],['Vik',68]]

ages = [['Aaron',15],['Dhruti',16]]
/#If we wanted to create a list of lists that paired each name with a height
#we could use the command zip. zip takes two (or more) lists as inputs and returns an object that contains a list of pairs.
#
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names,dogs_names)
#To print it´s neccesary convert the object into a list
print(list(name_and_dogs_names))
#We can add a single element to a list using .append(). 
