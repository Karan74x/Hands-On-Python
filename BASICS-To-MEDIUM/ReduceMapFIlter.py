#map
# def c_to_f(temp):
#     return (temp * 9/5) + 32
#
# def f_to_c(temp):
#     return (temp - 32) * 5/9

# celsius_temps = [0.0, 0.18, 25.07, 74.74, 74.75]
# rows = list(map(c_to_f, celsius_temps))
# print(rows)

#👆🏻👆🏻 map(function, collection) applies a given function to all items in a collection



# def passing(grade):
#     return grade >=60

# grades = [91,58,75,36,98]
# passing_grade = list(filter(lambda x: x>70,grades))
# print(passing_grade)
#👆🏻filter(function,collection) returns all elements that pass a condition




from functools import reduce

# def add(x,y):
#     return x+y

# prices = [85.45, 89.74, 74.74, 68, 75]
# # total = reduce(add,prices)
# total = reduce(lambda x,y:x+y,prices)
# print(total)
#


#👆🏻reduce(function, collection) = Reduces elements in a collection to a single value
#                                   for loop is better in most cases
#                                   reduce is better for a functional approach + readability
