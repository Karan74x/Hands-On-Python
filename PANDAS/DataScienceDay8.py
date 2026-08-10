import pandas as pd

students = pd.read_csv(r"../CSV FILES/students.csv")
fees = pd.read_csv(r"../CSV FILES/fees.csv")


#                  joins
# merge() → usually joins using columns
# join()  → joins using index


# StudentID → now becomes the index.
students = students.set_index("StudentID")
fees = fees.set_index("StudentID")


# Keep all rows from students.
# print(students.join(fees, how="left"))

#  Keep all rows from fees.
# print(students.join(fees, how="right"))

# how ="inner" ->Keep only IDs that exist in both tables.
print(students.join(fees, how="inner"))


# how="outer" -> Keep ALL rows from both DataFrames.
print(students.join(fees, how="outer"))``
