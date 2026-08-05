import pandas as pd

students = pd.read_csv(r"../CSV FILES/students.csv")

#                         groupby()
#used to group rows having similar values

# Group students according to City.

# for city,group in students.groupby("City"):
#   print("City: ",city)
#   print(group)

# Group students according to Department

# for dept, rows in students.groupby("Department"):
#   print("Department: ",dept )
#   print(rows)

#  Group students according to Marks
# for marks,stud in students.groupby("Marks"):
#   print("Marks: ",marks)
#   print(stud)


#                           calculations
#      mean(), sum(), count(), max(), min(), agg()


#                 mean()

Calculate average Marks for each City group
print(students.groupby("City")["Marks"].mean())



#                     sum()
# Adds all values in each group.

print(students.groupby("City")["Marks"].sum())
print(students.groupby("Department")["Marks"].sum())

#                   count()

#         Counts the number of values in each group.
print(students.groupby("Department")["Name"].count())
print(students.groupby("City")["Marks"].count())


#                     max()
#      Finds the highest value in every group.

print(students.groupby("Department")["Marks"].max())
print(students.groupby("City")["Marks"].max())


#               min()
#     Finds the smallest value in every gro

print(students.groupby("City")["Marks"].min())
print(students.groupby("Department")["Marks"].min())



#                           agg()
#               Apply multiple calculations at once.

print(students.groupby("Department")["Marks"].agg(["count","sum","mean","max","min"]))

print(students.groupby("City")["Marks"].agg(["sum","mean","max","count"]))
