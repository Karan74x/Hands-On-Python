import pandas as pd

students = pd.read_csv(r"../CSV FILES/students.csv")
fees = pd.read_csv(r"../CSV FILES/fees.csv")


#                  joins
# merge() → usually joins using columns
# join()  → joins using index


# StudentID → now becomes the index.
# students = students.set_index("StudentID")
# fees = fees.set_index("StudentID")


# Keep all rows from students.
# print(students.join(fees, how="left"))

#  Keep all rows from fees.
# print(students.join(fees, how="right"))

# how ="inner" ->Keep only IDs that exist in both tables.
# print(students.join(fees, how="inner"))


# how="outer" -> Keep ALL rows from both DataFrames.
# print(students.join(fees, how="outer"))



#                String functions
# Used to convert text to lowercase.
print(students["Name"].str.lower())


# Used to convert text to uppercase.
print(students["Name"].str.upper())


# Finds the length of each string.
print(students["Name"].str.len())


#emoves extra spaces from the beginning and end of a string.
print(students["Name"].str.strip())


# Used to check whether a string contains a particular word or character.
print(students["Name"].str.contains("r", case=False)) #You can make it case-insensitive with case=False


# Replace() -> Used to replace text inside strings.
 print(students["City"].str.replace('a','7'))



# startswith() -> Used to check whether a string starts with a particular character or text.
print(students["Name"].str.startswith("R"))


# str.endswith() checks whether a string ends with specific text.
# print(students)
print(students["City"].str.endswith('t'))
