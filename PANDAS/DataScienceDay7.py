import pandas as pd

students = pd.read_csv(r"../CSV FILES/students.csv")

new_students = pd.read_csv(r"../CSV FILES/new_students.csv")
fees = pd.read_csv(r"../CSV FILES/fees.csv")

#                 CONCAT()
# Used to combine DataFrames.


# objs -> [df1, df2]
# Means Which DataFrames do you want to combine

# print(pd.concat([students,new_students]))

# axis = 1
# print(pd.concat([fees,new_students], axis=1))

# ignore index
# print(pd.concat([students, new_students], ignore_index = True))


#                   Merge()
# Used to combine two DataFrames using one or more common columns.
# pd.merge(left, right, on, how)


#  Used to specify the common column for matching.
# print(pd.merge(students, fees, on="StudentID"))


#                 how() -> default how="inner"

# Keeps every row from the LEFT DataFrame.
print(pd.merge(students, fees,on="StudentID",how="left"))
print(pd.merge(fees,students,on="StudentID",how="left"))

# Keeps every row from the RIGHT DataFrame.
print(pd.merge(students, fees,on="StudentID",how="right"))
print(pd.merge(fees,students,on="StudentID",how="right"))

# Keeps every row from both DataFrames.
print(pd.merge(students, fees,on="StudentID",how="outer"))
print(pd.merge(fees,students,on="StudentID",how="outer"))
