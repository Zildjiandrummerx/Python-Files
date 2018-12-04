# create a function named num_teachers that takes a single argument, which will be a 
# dictionary of Treehouse teachers and their courses.
# The num_teachers function should return an integer for how many teachers are in the dict.

def num_teachers(teachers):
    count = 0
    for teacher in teachers:
        count += 1
    return count

# Create a new function named num_courses that will receive the same dictionary as its only argument.
# The function should return the total number of courses for all of the teachers.

def num_courses(teachers):
    num = 0
    for value in teachers.values():
        num += len(value)
    return num

# make another new function named courses that will, again, take the dictionary of teachers 
# and courses. Courses, though, should return a single list of all of the available courses 
# in the dictionary. No teachers, just course names!

def courses(teachers):
    course_output = []
    for course_total in teachers.values():
        for course in course_total:
            course_output.append(course)
    return course_output

# Create a function named most_courses that takes our good ol' teacher dictionary.
# most_courses should return the name of the teacher with the most courses. 
# You might need to hold onto some sort of max count variable.

def most_courses(teachers):
  most_class = ""     # holds the name of teach with most class
  max_count = 0       # max counter for classes
  for teacher in teachers:
    if len(teachers[teacher]) > max_count:
      max_count = len(teachers[teacher])
      most_class = teacher
  return most_class

# In this last challenge, I want you to create a function named stats and it'll take 
# our teacher dictionary as its only argument. stats should return a list of lists 
# where the first item in each inner list is the teacher's name and the second item 
# is the number of courses that teacher has. For example, it might return: 
# [["Kenneth Love", 5], ["Craig Dennis", 10]]

def stats(teachers):
    statslist = []
    for teacher, courses in teachers.items():
        total = 0
        for value in teachers.values():
            for course in value:
                total += 1
                statslist.append([teacher, total])
    return statslist

# To check later: https://teamtreehouse.com/community/list-of-lists-function