last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]

gradebook = list(zip(grades, subjects))
gradebook.append(("visual arts",93))

print(list(gradebook))
#add another value
subjects.append("computer science")
grades.append(100)

#If you want to add two list
full_gradebook = gradebook + last_semester_gradebook

#Range II
#With one or two arguments, range will create a list of consecutive numbers (i.e., each number is one greater than the previous number). If we use a third argument, we can create a list that “skips” numbers.
# For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:
>>> my_range2 = range(2, 9, 2)
>>> print(list(my_range2))
[2, 4, 6, 8]
