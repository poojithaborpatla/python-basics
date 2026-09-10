


# TASK 1: TOKENS & STATEMENTS

name = "Poojitha"
age = 25
city = "Guntur"

print("Name:", name)   # Output: Name: Poojitha
print("Age:", age)     # Output: Age: 25
print("City:", city)   # Output: City: hyderbad



# TASK 2: IDENTIFIERS
student_name = "Poojitha"
student_age = 25
student_marks = 65
print("Student Name:", student_name)    # Output: Student Name: Poojitha
print("Student Age:", student_age)      # Output: Student Age: 25
print("Student Marks:", student_marks)  # Output: Student Marks: 65

# student-name = "Poojitha"
# Invalid because '-' is not allowed in Python identifiers.

# TASK 3: SINGLE-LINE COMMENTS
# Stores the student's name
name = "Poojitha"

# Stores the student's age
age = 25

print("Name:", name)  # Output: Name: Poojitha
print("Age:", age)    # Output: Age: 25

# TASK 4: MULTI-LINE COMMENTS

# This program prints
# three messages about
# learning Python.

print("Welcome to Python")              # Output: Welcome to Python
print("I am learning programming")      # Output: I am learning programming
print("Python is easy to learn")        # Output: Python is easy to learn

# TASK 5: VARIABLES

name = "Poojitha"
age = 25
height = 5.4
is_student = True
print("Name:", name)              # Output: Name: Poojitha
print("Age:", age)                # Output: Age: 25
print("Height:", height)          # Output: Height: 5.4
print("Is Student:", is_student)  # Output: Is Student: True

# TASK 6: MULTIPLE ASSIGNMENT
name, age, city = "Poojitha", 25, "Guntur"

print("Name:", name)   # Output: Name: Poojitha
print("Age:", age)     # Output: Age: 25
print("City:", city)   # Output: City: hyderbad


# TASK 7: REASSIGNMENT

age = 25
print("Current Age:", age)  # Output: Current Age: 25
age = 26
print("New Age:", age)      # Output: New Age: 26


# TASK 8: SWAPPING VARIABLES

a = 10
b = 20
print("Before:", a, b)  # Output: Before: 10 20
a, b = b, a
print("After:", a, b)   # Output: After: 20 10


# TASK 9: DELETING VARIABLES

name = "Poojitha"
print("Name:", name)  # Output: Name: Poojitha
del name

# print(name)
# Output: NameError: name 'name' is not defined

# TASK 10: KEYWORDS

import keyword

print("Python Keywords:", keyword.kwlist)
# Output: Python keyword list

print("Total Number of Keywords:", len(keyword.kwlist))
# Output: Depends on the Python version
#
#