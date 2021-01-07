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
